import xlrd
from xlutils.copy import copy

#<basic-form table-name="basic-plan-basic-information" title="基本方案-基本信息" :pdf-id="pdfId"></basic-form>

readbook = xlrd.open_workbook('Data0325_translate.xls', formatting_info=True)
sheet = readbook.sheet_by_index(4)  # 索引的方式，从0开始
nrows = sheet.nrows  # 行
ncols = sheet.ncols  # 列
new_form = False
for x in range(3, nrows):
  word = str(sheet.cell(x, 1).value).strip()
  trans = str(sheet.cell(x, 2).value).strip()
  word_type = str(sheet.cell(x, 3).value).strip()
  if '-' in word.strip():
    new_form = True
    if 'form' in word:
      print('<basic-form table-name="'+trans+'" :pdf-id="pdfId" title="'+sheet.name+'-'+word.replace('-form','')+'" :company-package-id="item.row_id"></basic-form>')
    if 'table' in word:
      print('<basic-table table-name="'+trans+'" :pdf-id="pdfId" title="'+sheet.name+'-'+word.replace('-table','')+'" :company-package-id="item.row_id"></basic-table>')
    continue
new_form = False
