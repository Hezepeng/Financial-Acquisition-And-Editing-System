import re

import requests
import string
import time
import hashlib
import json
import xlrd
from xlutils.copy import copy

# init
api_url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
my_appid = '20190318000278434'
cyber = 'eDjUeCORXJkzXffr7JNN'
lower_case = list(string.ascii_lowercase)


def requests_for_dst(w):
  word = w
  word = str(word).replace("是否", "").replace("-table", "").replace("-form", "").replace("-checkbox", "").replace("-", "_").replace('/', '_').replace(" ", "")
  word = word.replace('(', '（').replace(')', '）')
  word = re.sub(r"(（.*）$)", "", word)
  words = word.split("_")
  salt = str(time.time())[:10]
  domain = 'electronics'
  final_sign = str(my_appid) + word + salt + cyber
  final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
  # 区别en,zh构造请求参数
  paramas = {
    'q': word,
    'from': 'zh',
    'to': 'en',
    'appid': '%s' % my_appid,
    'salt': '%s' % salt,
    'sign': '%s' % final_sign
  }
  my_url = api_url + '?appid=' + str(my_appid) + '&q=' + word + '&salt=' + salt + '&sign=' + final_sign
  response = requests.get(api_url, params=paramas).content
  content = str(response, encoding="utf-8")
  json_reads = json.loads(content)
  # print(content)
  res = str(json_reads['trans_result'][0]['dst'])
  # print(res)
  res = res.lower().replace('/', '').replace("-", "_").replace("'s", " ").replace("s'", " ").replace(" and", "").replace(",", " ").replace("、", " ").replace(".", "").replace("?", "").replace("the ", "").replace(" a ", " ").replace("is ", "").replace(" ", "_").replace("_____", "_") \
    .replace("____", "_").replace("___", "_").replace("__", "_")
  print(res)
  res = res.replace('1', 'one').replace('2', 'two').replace('3', 'three').replace('4', 'four').replace('5', 'five')
  res = inverted_of(res)
  res = inverted_for(res)
  return res


def inverted_of(sen):
  sen = str(sen)
  if '_of_' not in sen:
    return sen
  start = sen[:sen.index('_of_')]
  # print(start)
  end = sen[sen.index('_of_') + 4:]
  # print(end)
  sen = end + '_' + start
  if '_of_' not in sen:
    return inverted_of(sen)
  print(sen)
  return sen


def inverted_for(sen):
  sen = str(sen)
  if '_for_' not in sen:
    return sen
  start = sen[:sen.index('_for_')]
  # print(start)
  end = sen[sen.index('_for_') + 5:]
  # print(end)
  sen = end + '_' + start
  if '_for_' not in sen:
    return inverted_for(sen)
  print(sen)
  return sen


dictionary = {
  '标的资产交割': 'assets_delivery',
  '标的资产': 'underlying assets',
  '支付方式': 'payment',
  '发行可转债': 'bonds',
  '交易完成后的整合': 'integration',
  '高级管理人员': 'senior',
  '标的公司': 'target_company',
  '股份有限公司': 'limited_company',
  '股份公司': 'share_company',
  '有限公司': 'limited_company',
  '过渡期': 'transition',
  '控股股东': 'shareholder',
  '股东': 'shareholder',
  '实际控制人': 'controller',
  '发起人': 'sponsor',
  '股权': 'stock',
  '股份': 'share',
  '解禁上市': 'to_sale',
  '补偿义务分配': 'compensation',
  '账户内资金': 'funds',
  '计算公式': 'calculation_formula',
  '承诺长期应收款周转率': 'commit_long_term_turnover_ratio',
  '承诺长期应收款回收率': 'commitment_long-term_recovery_ratio',
  '承诺应收账款回收率': 'commitment_receivables_recovery_ratio',
  '业绩承诺':'performance_commitment',
}

readbook = xlrd.open_workbook(r'Data0325.xls', formatting_info=True)
writebook = copy(readbook)
for i in range(0, 8):
  new_sheet = writebook.get_sheet(i)
  sheet = readbook.sheet_by_index(i)  # 索引的方式，从0开始
  nrows = sheet.nrows  # 行
  ncols = sheet.ncols  # 列
  for x in range(3, nrows):
    word = str(sheet.cell(x, 1).value).strip()
    trans = str(sheet.cell(x, 2).value).strip()
    word_type = str(sheet.cell(x, 3).value).strip()
    word = word.replace('-table', '').replace('-form', '').replace('-checkbox', '')
    if str(word).strip() is not "":
      for item in dictionary.keys():
        if item in word:
          word = word.replace(item, dictionary[item])
      print(word)
      if word == '文件ID':
        res = 'pdf_id'
      elif word == '公司ID':
        res = 'company_id'
      elif word == "表格序号":
        res = 'row_id'
      else:
        res = ''
        for item in word.split('-'):
          res += requests_for_dst(item) + '_'
        res = res.strip('_')
        if word_type == 'checkbox':
          res += '_flag'
        while len(res) > 62:
          res = res[res.index('_') + 1:]
      new_sheet.write(x, 2, res)
      print(res)
writebook.save(u'Data0325_translate.xls')

# if __name__ == '__main__':
#   while True:
#     s = str(input("输入:"))
#     print(s.lower().replace("-", "_").replace("'s", " ").replace("s'", " ").replace(" and", "").replace(",", " ").replace("、", " ").replace(".", "").replace("?", "").replace("the ", "").replace(" a ", " ").replace("is ", "").replace(" ", "_").replace("__", "_").replace("__", "_"))
