from json import dumps
import xlrd
from xlutils.copy import copy

readbook = xlrd.open_workbook('Data0325_translate.xls', formatting_info=True)

for i in range(0, 8):
  last_trans = ''
  type_dic = {}
  new_form = False
  sheet = readbook.sheet_by_index(i)  # 索引的方式，从0开始
  nrows = sheet.nrows  # 行
  ncols = sheet.ncols  # 列
  for x in range(3, nrows):
    word = str(sheet.cell(x, 1).value).strip()
    trans = str(sheet.cell(x, 2).value).strip()
    word_type = str(sheet.cell(x, 3).value).strip()
    if word is "" and new_form is False:
      continue
    if word == "文件ID" or word == "表格序号" or word == '公司ID':
      continue
    if word is "" and new_form is True:
      print("}")
      print()
      print(last_trans + "_key_type_list =", dumps(type_dic, indent=2))
      print()
      new_form = False
      type_dic = {}
      continue
    if '-form' in word or '-table' in word:
      new_form = True
      last_trans = trans
      print()
      print("#", word)
      print(trans + "_key_value_list = {")
      continue
    elif str(word) is "":
      print()
      continue
    else:
      print('  "' + trans + '":' + ' "' + word + '",')
      if 'double' in word_type:
        word_type = 'decimal'
      type_dic[trans] = word_type
  print("}")
  print()
  print(last_trans + "_key_type_list =", dumps(type_dic, indent=2))
