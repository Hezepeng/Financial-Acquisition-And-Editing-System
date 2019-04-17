import json
import os

from django.core import serializers

from DataEntrySystem.dataConfig import *
from django.http import HttpResponse
from django.shortcuts import render
from DataEntrySystem.utils import *
import hashlib

from DataEntrySystem.models import basic_plan_essential_information, target_company_package, target_company_used_in_package, pdf_information


def get_key_value_list(request):
  formName = request.GET.get("tableName", None)
  formName = str(formName).replace('-', '_')
  keyValueListName = formName + "_key_value_list"
  keyTypeListName = formName + "_key_type_list"
  data = {
    'code': 1,
    'keyTypeList': get_data_config(keyTypeListName),
    'keyValueList': get_data_config(keyValueListName)
  }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


def change_single_obj_to_json(obj):
  obj_dict = obj.__dict__
  del obj_dict['_state']
  return obj_dict


def get_form_data(request):
  tableName = request.GET.get("tableName", None)
  pdfId = request.GET.get("pdfId", None)
  companyPackageId = int(request.GET.get("companyPackageId", -1))
  if companyPackageId == -1:
    companyPackageId = None
  tableName = str(tableName).replace('-', '_')
  db_table = get_model_class(tableName)
  obj, created = db_table.objects.get_or_create(pdf_id=str(pdfId), company_package_id=companyPackageId, defaults={'pdf_id': str(pdfId), 'company_package_id': companyPackageId})
  data = {
    'code': 1,
    'formData': object_to_json(obj)
  }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


def get_table_data(request):
  tableName = request.GET.get("tableName", None)
  pdfId = request.GET.get("pdfId", None)
  companyPackageId = int(request.GET.get("companyPackageId", -1))
  if companyPackageId == -1:
    companyPackageId = None
  tableName = str(tableName).replace('-', '_')
  db_table = get_model_class(tableName)
  obj = db_table.objects.filter(pdf_id=str(pdfId), company_package_id=companyPackageId).order_by('row_id')
  data = {
    'code': 1,
    'tableData': object_to_json(obj)
  }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


def get_table_row_data(request):
  tableName = request.GET.get("tableName", None)
  pdfId = request.GET.get("pdfId", None)
  rowId = request.GET.get("rowId", None)
  tableName = str(tableName).replace('-', '_')
  db_table = get_model_class(tableName)
  obj, created = db_table.objects.filter(pdf_id=str(pdfId), row_id=rowId).first()
  data = {
    'code': 1,
    'formData': object_to_json(obj)
  }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


def save_single_data(request):
  tableName = request.POST.get("tableName", None)
  pdfId = request.POST.get("pdfId", None)
  rowId = request.POST.get("rowId", None)
  field = request.POST.get("field", None)
  content = request.POST.get("editContent", None)
  if content is '':
    content = None
  companyPackageId = int(request.POST.get("companyPackageId", -1))
  if companyPackageId == -1:
    companyPackageId = None
  if content == "true" or content == "false":
    content = True if content.lower() == "true" else False
  # 找到数据库表对象
  tableName = str(tableName).replace('-', '_')
  db_table = get_model_class(tableName)
  obj = db_table.objects.filter(pdf_id=str(pdfId), row_id=rowId).first()
  data = {
    'code': 1
  }
  if obj is not None:
    obj.set_attr(field, content)
    obj.save()
  else:
    data = {
      'code': -1
    }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


def save_table_row_data(request):
  postData = json.loads(request.body)
  rowData = postData['rowData']
  tableName = postData['tableName']
  # if content == "true" or content == "false":
  #   content = True if content.lower() == "true" else False
  # 找到数据库表对象
  tableName = str(tableName).replace('-', '_')
  db_table = get_model_class(tableName)
  if int(rowData['company_package_id']) == -1:
    rowData['company_package_id'] = None
  obj = db_table(**rowData)
  obj.save()
  data = {
    'code': 1,
    'data': object_to_json(obj)
  }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


def delete_table_row_data(request):
  postData = json.loads(request.body)
  rowData = postData['rowData']
  rowId = rowData['row_id']
  tableName = postData['tableName']
  tableName = str(tableName).replace('-', '_')
  db_table = get_model_class(tableName)
  # 如果是删除标的公司
  if tableName == "basic_plan_essential_information":
    pdfId = rowData['pdf']
    companyPackage = target_company_package.objects.filter(pdf_id=pdfId)
    for item in companyPackage:
      company_id_list = [int(i) for i in item.get_attr('company_id_list')]
      if rowId in company_id_list:
        for company_id in company_id_list:
          for used_company in target_company_used_in_package.objects.filter(pdf_id=pdfId, company_id=company_id):
            used_company.set_attr('used_flag',False)
            used_company.save()
        item.delete()
  db_table.objects.filter(row_id=rowId).delete()
  data = {
    'code': 1,
  }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


# 获取某个pdf的信息 如果参数为空 则获取所有pdf信息
def get_pdf(request):
  tableName = request.GET.get("tableName", None)
  pdfId = request.GET.get("pdfId", None)
  tableName = str(tableName).replace('-', '_')
  db_table = get_model_class(tableName)
  data = dict()
  if not pdfId:
    obj = db_table.objects.all().order_by('create_time')
    data = {
      'code': 1,
      'tableData': object_to_json(obj)
    }
  else:
    obj = db_table.objects.filter(pdf_id=str(pdfId)).first()
    data = {
      'code': 1,
      'tableData': single_object_to_json(obj)
    }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


# 上传并保存pdf
def upload_pdf(request):
  file = request.FILES.get('file')
  file_name = file.name
  pdf_id = hashlib.md5(file_name.encode(encoding='UTF-8')).hexdigest()
  # 找到数据库表对象
  pdf = dict()
  pdf['pdf_id'] = pdf_id
  pdf['full_name'] = file_name
  pdf['create_time'] = datetime.datetime.now()
  pdf['simple_name'] = ''
  obj = pdf_information.objects.filter(pdf_id=str(pdf_id)).first()
  data = dict()
  if obj is None:
    obj = pdf_information(**pdf)
    obj.save()
    data['code'] = 1
    # data['file'] = single_object_to_json(obj)
  else:
    data['code'] = 0
    # data['file'] = single_object_to_json(obj)
  # f = open(os.path.join('upload', obj.name), 'wb')
  # for line in obj.chunks():
  #   f.write(line)
  # f.close()
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


# 获取某个pdf所有的标的公司
def get_all_company(request):
  pdfId = request.GET.get("pdfId", None)
  moduleName = request.GET.get("moduleName", None)
  data = dict()
  objs = basic_plan_essential_information.objects.filter(pdf_id=str(pdfId)).order_by('row_id')
  for item in objs:
    if target_company_used_in_package.objects.filter(pdf_id=pdfId, module_name=moduleName, company_id=item.get_attr('row_id')).first() is None:
      company_use = dict()
      company_use['pdf_id'] = pdfId
      company_use['company_id'] = item.get_attr('row_id')
      company_use['module_name'] = moduleName
      company_use['used_flag'] = False
      company_use_obj = target_company_used_in_package(**company_use)
      company_use_obj.save()
  res = target_company_used_in_package.objects.filter(pdf_id=pdfId, module_name=moduleName).order_by('company_id')
  data = {
    'code': 1,
    'data': object_to_json(res)
  }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


# 获取某个pdf的所有标的公司组合
def get_all_company_package(request):
  pdfId = request.GET.get("pdfId", None)
  moduleName = request.GET.get("moduleName", None)
  db_table = target_company_package
  data = dict()
  obj = db_table.objects.filter(pdf_id=str(pdfId), module_name=moduleName).order_by('row_id')
  data = {
    'code': 1,
    'data': object_to_json(obj)
  }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


# 保存标的公司组合
def save_company_package(request):
  postData = json.loads(request.body)
  pdfId = postData["pdfId"]
  moduleName = postData["moduleName"]
  packageName = postData["packageName"]
  companyList = list(postData["companyList"])
  package = dict()
  package['pdf_id'] = pdfId
  package['module_name'] = moduleName
  package['package_name'] = packageName
  package['company_id_list'] = companyList
  package['create_time'] = datetime.datetime.now()
  db_table = target_company_package
  obj = db_table(**package)
  obj.save()
  for company_id in companyList:
    company_use_obj = target_company_used_in_package.objects.filter(pdf_id=pdfId, module_name=moduleName, company_id=company_id).first()
    company_use_obj.set_attr('used_flag', True)
    company_use_obj.save()
  data = {
    'code': 1,
    'data': object_to_json(obj)
  }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


# 删除套件标的公司组合
def delete_company_package(request):
  postData = json.loads(request.body)
  row_id = postData["rowId"]
  data = delete_company_package_fun(row_id)
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")


# 删除套件标的公司组合函数
def delete_company_package_fun(row_id):
  package = dict()
  db_table = target_company_package
  obj = db_table.objects.filter(row_id=int(row_id)).first()
  moduleName = obj.get_attr('module_name')
  for company_id in obj.get_attr('company_id_list'):
    company = target_company_used_in_package.objects.filter(company_id=int(company_id), module_name=moduleName).first()
    company.set_attr('used_flag', False)
    company.save()
  # TODO 删除所有包含标的公司组合的表的数据
  obj.delete()
  data = {
    'code': 1,
    'data': object_to_json(obj)
  }
  return data


def delete_pdf(request):
  pdfId = request.GET.get("pdfId", None)
  pdf = pdf_information.objects.filter(pdf_id=pdfId).first()
  if pdf:
    pdf.delete()
  data = {
    'code': 1
  }
  return HttpResponse(json.dumps(data, ensure_ascii=False, indent=2, cls=MyEncoder), content_type="application/json")
