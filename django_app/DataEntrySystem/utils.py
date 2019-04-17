import datetime
import decimal
import importlib
import json

from django.db.models.query import QuerySet

from DataEntrySystem.models import pdf_information, basic_plan_essential_information, target_company_package, target_company_used_in_package


# 根据变量名获取变量
def get_data_config(obj_name):
  module_manager = importlib.import_module('DataEntrySystem.dataConfig')
  obj = getattr(module_manager, obj_name)
  return obj


# 根据表名获取数据库表对象
def get_model_class(class_name):
  module_manager = importlib.import_module('DataEntrySystem.models')
  model_class = getattr(module_manager, class_name)
  return model_class


def object_to_json(model, ignore=None):
  if ignore is None:
    ignore = []
  if type(model) in [QuerySet, list]:
    json = []
    for element in model:
      json.append(single_object_to_json(element, ignore))
    return json
  else:
    return single_object_to_json(model, ignore)


def single_object_to_json(element, ignore=None):
  return dict([(attr, getattr(element, attr)) for attr in [f.name for f in element._meta.fields if f not in ignore]])


def change_single_obj_to_json(obj):
  obj_dict = obj.__dict__
  del obj_dict['_state']
  return obj_dict


class MyEncoder(json.JSONEncoder):
  def default(self, o):
    if isinstance(o, datetime.datetime):
      return o.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(o, datetime.date):
      return o.strftime("%Y-%m-%d")
    elif isinstance(o, decimal.Decimal):
      return float(o)
    elif isinstance(o, pdf_information):
      return o.pdf_id
    elif isinstance(o, basic_plan_essential_information):
      return change_single_obj_to_json(o)
    elif isinstance(o,target_company_package):
      return change_single_obj_to_json(o)
    elif isinstance(o,target_company_used_in_package):
      return change_single_obj_to_json(o)
    else:
      return json.JSONEncoder.default(self, o)


def init_date_field(model):
  for element in model:
    print(type(element))
    print(element)
