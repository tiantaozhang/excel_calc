import codecs

# read excel to dateset
import shutil
import xlrd
import xlwt
from  tempfile import TemporaryFile


class Excel:
    def __init__(self, path):
        self.path = path

    def changePath(self, path):
        self.path = path

    # return {"sheet1": [[,,,,],[]], "sheet2": []}
    def read(self):
        data = xlrd.open_workbook(self.path)
        sheets = {}
        for s in data.sheets():
            # print 'Sheet:', s.name
            sheets[s.name] = []
            for row in range(s.nrows):
                values = []
                for col in range(s.ncols):
                    values.append(s.cell(row, col).value)
                # print ','.join(str(values))
                sheets[s.name].append(values)
        return sheets

    # sheet: [sheet1,sheet2,...], {"sheet1": [[,,,,,],[],...],"sheet2": [[],[],...]}
    def write(self, pwd, sheets, contents):
        book = xlwt.Workbook()
        for sheet in sheets:
            sheet_tmp = book.add_sheet(sheet)
            content_sheet = contents[sheet]
            for row in range(len(content_sheet)):
                print row, content_sheet[row]
                for col in range(len(content_sheet[row])):
                    sheet_tmp.write(row, col, content_sheet[row][col])
            sheet_tmp.flush_row_data()
        book.save(pwd)
        # book.save(TemporaryFile())

        # book = xlwt.Workbook()
        # sheet1 = book.add_sheet('Sheet 1')
        # book.add_sheet('Sheet 2')
        # sheet1.write(0, 0, 'A1')
        # sheet1.write(0, 1, 'B1')
        # row1 = sheet1.row(1)
        # row1.write(0, 'A2')
        # row1.write(1, 'B2')
        #
        # sheet1.col(0).width = 10000
        # sheet2 = book.get_sheet(1)
        # sheet2.row(0).write(0, 'Sheet 2 A1')
        # sheet2.row(0).write(1, 'Sheet 2 B1')
        # sheet2.flush_row_data()
        #
        # sheet2.write(1, 0, 'Sheet 2 A3')
        # sheet2.col(0).width = 5000
        # sheet2.col(0).hidden = True
        # book.save(pwd)
        # book.save(TemporaryFile())
