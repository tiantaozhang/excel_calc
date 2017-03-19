# -*- coding: utf-8 -*-

from unittest import TestCase
from lib.excel import Excel
import pprint

class TestExcel(TestCase):
    def test_read(self):
        exl = Excel('/Users/tatumn/home/workspace/python/github.com/tiantaozhang/excel_calc/test/data/快递费用明细.xlsx')
        sheets = exl.read()
        print sheets
        exl.changePath('/Users/tatumn/home/workspace/python/github.com/tiantaozhang/excel_calc/test/simple1.xls')
        sheets = exl.read()
        pprint.pprint(sheets)

    def test_write(self):
        exl = Excel('/Users/tatumn/home/workspace/python/github.com/tiantaozhang/excel_calc/test/data/产品报价明细.xlsx')
        pwd = '/Users/tatumn/home/workspace/python/github.com/tiantaozhang/excel_calc/test/simple1.xls'
        exl.write(pwd, [u'表格1',u'sheet2'], {u'表格1': [[u'a','bc',u'结果',u'会是怎样呢'],[u'哈哈','bc','ddd'],['sasd','fda'],[u'好的',u'好的',u'好的',u'好的']],
                                          'sheet2': [['test',u'测试'],[u'测试', u'😀']]})