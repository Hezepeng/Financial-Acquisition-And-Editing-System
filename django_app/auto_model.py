import xlrd
from xlutils.copy import copy

readbook = xlrd.open_workbook('Data0325_translate.xls', formatting_info=True)
for i in range(0, 8):
  sheet = readbook.sheet_by_index(i)  # 索引的方式，从0开始
  nrows = sheet.nrows  # 行
  ncols = sheet.ncols  # 列
  new_form = False
  for x in range(3, nrows):
    word = str(sheet.cell(x, 1).value).strip()
    trans = str(sheet.cell(x, 2).value).strip()
    word_type = str(sheet.cell(x, 3).value).strip()
    if word is "" and new_form is False:
      continue
    if word is "" and new_form is True:
      print()
      print('  def get_attr(self, attr_name):')
      print('    return getattr(self, attr_name)')
      print()
      print('  def set_attr(self, attr_name, content):')
      print('    setattr(self, attr_name, content)')
      print('    return')
      print()
      new_form = False
      continue
    if '-form' in word or '-table' in word:
      new_form = True
      print()
      print("#", word)
      print("class " + trans + "(models.Model):")
      print("  class Meta:")
      print('    db_table = "' + trans + '"')
      print()
      continue
    elif str(word) is "":
      print()
      continue
    else:
      if trans == "row_id":
        print('  row_id = models.AutoField(primary_key=True)')
      elif trans == "company_package_id":
        print('  company_package = models.ForeignKey("target_company_package", on_delete=models.CASCADE, null=True, default=None)')
      elif trans == "pdf_id":
        print('  pdf = models.ForeignKey("pdf_information", on_delete=models.CASCADE, null=False, blank=False)')
      elif word_type is "" or word_type == "text":
        print("  " + trans + " = models.TextField(blank=True, null=True)")
      elif word_type == "checkbox":
        print("  " + trans + ' = models.BooleanField(blank=False, null=False, default=False)')
      elif word_type == "datetime":
        print("  " + trans + ' = models.DateField(blank=True, null=True)')
      elif 'double' in word_type or 'ratio' in word_type:
        print("  " + trans + ' = models.DecimalField(blank=True,null=True,max_digits=25, decimal_places=2)')
      else:
        print("  " + trans + " = models.TextField(blank=True, null=True)")
  print()
  print('  def get_attr(self, attr_name):')
  print('    return getattr(self, attr_name)')
  print('  def set_attr(self, attr_name, content):')
  print('    setattr(self, attr_name, content)')
  print('    return')
  print()
