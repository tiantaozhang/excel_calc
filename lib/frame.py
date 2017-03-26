# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox
import Tkinter
import tkFileDialog
from lib.excel import Excel
import os
import logging
# from log.log import Log

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.__excel = Excel("")
        self.grid()
        self.e1 = StringVar()
        self.e2 = StringVar()
        self.e3 = StringVar()
        self.e4 = StringVar()
        self.eResult = StringVar()
        self.createWidgets()
        logging.basicConfig(filename='excel.txt', level=logging.INFO, filemode='w')

    def createWidgets(self):
        Label(self, text='产品报价明细:', font=(
            'Arial', 12)).grid(row=0, sticky='nw', padx=20, pady=20)
        Label(self, text='店铺销售明细:', font=(
            'Arial', 12)).grid(row=1,  sticky='nw', padx=20, pady=20)
        Label(self, text='快递单号明细:', font=(
            'Arial', 12)).grid(row=2, column=0, sticky='nw', padx=20, pady=20)
        Label(self, text='快递费用明细:', font=(
            'Arial', 12)).grid(row=3,column=0, sticky='nw', padx=20, pady=20)
        self.entry1 = Entry(self, textvariable=self.e1)
        self.entry2 = Entry(self, textvariable=self.e2)
        self.entry3 = Entry(self, textvariable=self.e3)
        self.entry4 = Entry(self, textvariable=self.e4)
        self.setEntryAttribute(self.entry1, self.entry2, self.entry3, self.entry4, width=70)

        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.entry3.grid(row=2, column=1)
        self.entry4.grid(row=3, column=1)

        self.button1 = Button(self, text=u'...', command=self.getFile(self.entry1))
        self.button2 = Button(self, text=u'...', command=self.getFile(self.entry2))
        self.button3 = Button(self, text=u'...', command=self.getFile(self.entry3))
        self.button4 = Button(self, text=u'...', command=self.getFile(self.entry4))
        self.button1.grid(row=0, column=6, sticky=E, padx=20, ipadx=5)
        self.button2.grid(row=1, column=6, sticky=E, padx=20, ipadx=5)
        self.button3.grid(row=2, column=6, sticky=E, padx=20, ipadx=5)
        self.button4.grid(row=3, column=6, sticky=E, padx=20, ipadx=5)

        self.buttonResult = Button(self, text=u'计算结果', command=self.calculateResult)
        self.buttonResult.grid(row=5, column=0, sticky=NW, ipadx=5, ipady=5, padx=25, pady=50)

        self.entryResult = Entry(self, textvariable=self.eResult, width=70)
        self.entryResult.grid(row=5, column=1, pady=50)

    def calculateResult(self):
        self.e1.set('/Users/tatumn/home/workspace/python/github.com/tiantaozhang/excel_calc/test/testlog/产品报价明细.xlsx')
        self.e2.set('/Users/tatumn/home/workspace/python/github.com/tiantaozhang/excel_calc/test/testlog/店铺销售明细.xls')
        self.e3.set('/Users/tatumn/home/workspace/python/github.com/tiantaozhang/excel_calc/test/testlog/快递单号明细.xlsx')
        self.e4.set('/Users/tatumn/home/workspace/python/github.com/tiantaozhang/excel_calc/test/testlog/快递费用明细.xlsx')
        proDetail = self.getSheet(self.e1.get(), 'sheet1')
        sailDetail = self.getSheet(self.e2.get(), 'sheet1')
        expressNumberDetail = self.getSheet(self.e3.get(), 'sheet1')
        expressCostDetail = self.getSheet(self.e4.get(), 'sheet1')
        proDict = {}
        sailDict = {}
        expressNumDict = {}
        expreCostDict = {}
        #todo not sailDetail
        if sailDetail:
            # 货号
            goodsIndex, numberIndex, shopIndex = -1, -1, -1
            for index in range(len(sailDetail[0])):
                if u'货号' == sailDetail[0][index].strip():
                    # 货号 => 数量
                    goodsIndex = index
                elif u'数量' == sailDetail[0][index].strip():
                    numberIndex = index
                elif u'店铺名称' == sailDetail[0][index].strip():
                    shopIndex = index
            if goodsIndex == -1 or numberIndex == -1 or shopIndex == -1:
                # todo
                logging.info("销售明细找不到货号、数量或店铺名称，请检查")
                # tkMessageBox._show("销售明细找不到货号、数量或店铺名称，请检查")
                return

            for row in sailDetail[1:]:
                if row[shopIndex] in sailDict:
                    sailDict[row[shopIndex]].update({row[goodsIndex]: int(row[numberIndex])})
                else:
                    sailDict[row[shopIndex]] = {row[goodsIndex]: int(row[numberIndex])}

        # todo not proDetail
        if proDetail:
            index, goodsIndex, inPriceIndex, distributePriceIndex, brandIndex  = 0, -1, -1, -1, -1
            for index in range(len(proDetail[0])):
                if u'货号' == proDetail[0][index].strip():
                    goodsIndex = index
                elif u'进货价格' == proDetail[0][index].strip():
                    inPriceIndex = index
                elif u'分销价格' == proDetail[0][index].strip():
                    distributePriceIndex = index
                elif u'品牌' == proDetail[0][index].strip():
                    brandIndex = index

            if goodsIndex == -1 or inPriceIndex == -1 or distributePriceIndex == -1 or brandIndex == -1:
                # todo
                logging.info("产品明细找不到货号、进货价格、分销价格或品牌，请检查")
                return

            for row in proDetail[1:]:
                proDict[row[goodsIndex]] = {'inPrice': float(row[inPriceIndex]), 'distributePrice': float(row[distributePriceIndex]), 'brand': row[brandIndex]}

        # todo not expressNumberDetail
        if expressNumberDetail:
            index, expressNumIndex, shopIndex = 0, -1, -1
            for index in range(len(expressNumberDetail[0])):
                if u'快递单号' == expressNumberDetail[0][index].strip():
                    expressNumIndex = index
                elif u'店铺名称' == expressNumberDetail[0][index].strip():
                    shopIndex = index
            if expressNumIndex == -1 or shopIndex == -1:
                # todo
                logging.info("快递单号明细找不到快递单号或店铺名称，请检查")

            for row in expressNumberDetail[1:]:
                expressNumDict[int(row[expressNumIndex])] = row[shopIndex]

        # todo not expressCostDetail
        if expressCostDetail:
            index, expressNumIndex, costIndex = 0, -1, -1
            for index in range(len(expressCostDetail[0])):
                if u'快递单号' == expressCostDetail[0][index].strip():
                    expressNumIndex = index
                elif u'费用' == expressCostDetail[0][index].strip():
                    costIndex = index
            if expressNumIndex == -1 or costIndex == -1:
                # todo
                logging.info("快递费用明细找不到快递单号，费用，请检查")

            for row in expressCostDetail[1:]:
                expreCostDict[int(row[expressNumIndex])] = float(row[costIndex])

        dir = os.path.dirname(self.e1.get())
        dir += '/result.xls'
        result = self.dealData(sailDict, proDict, expressNumDict, expreCostDict)
        self.__excel.write(dir, [u'sheet1'], {u'sheet1': result})

        self.eResult.set(dir)

    def dealData(self, sailDict, proDict, expressNumDict, expressCostDetail):
        result = {}
        for shop, sail in sailDict.items():
            print '1111', shop, sail
            for proNum, amount in sail.items():
                if proNum in proDict:
                    inPrice = amount * proDict[proNum]['inPrice']
                    disPrice = amount * proDict[proNum]['distributePrice']

                    if shop in result:
                        if proDict[proNum]['brand'] in result[shop]:
                            result[shop][proDict[proNum]['brand']]['sumInPrice'] += inPrice
                            result[shop][proDict[proNum]['brand']]['sumDisPrice'] += disPrice
                        else:
                            result[shop][proDict[proNum]['brand']] = {'sumInPrice': inPrice, 'sumDisPrice': disPrice}
                    else:
                        result[shop] = {proDict[proNum]['brand']: {'sumInPrice': inPrice, 'sumDisPrice': disPrice}}
                else:
                    logging.warn(u'货号：%d   not found' % proNum)

        expressShop = {}
        totalCost = 0
        for expressNum, cost in expressCostDetail.items():
            if expressNum in expressNumDict:
                if expressNumDict[expressNum] in expressShop:
                    expressShop[expressNumDict[expressNum]] += cost
                else:
                    expressShop[expressNumDict[expressNum]] = cost
                totalCost += cost
            else:
                logging.warn('快递号：%d   not found' % expressNum)

        excelData = [[u'店铺名称', u'品牌', u'快递费用', u'分销成本', u'进货成本']]
        for shop in result.keys():
            for brand, value in result[shop].items():
                # if brand == 'expressCost':
                #     continue
                expressCost = 0
                if shop in expressShop:
                    expressCost = expressShop[shop]
                tmp = [shop, brand, expressCost, value['sumDisPrice'], value['sumInPrice']]
                excelData.append(tmp)

        return excelData

    def getSheet(self, path, sheet):
        self.__excel.changePath(path)
        sheetDict = self.__excel.read()
        if sheet in sheetDict:
            return sheetDict[sheet]
        else:
            return None

    # self.entry1['width'] = 15
    # self.entry1['show'] = '*'
    # entry['state'] = 'normal'
    # entry['state'] = 'readonly'
    def setEntryAttribute(self, *args, **kwargs):
        for entry in args:
            for key, value in kwargs.items():
                entry[key] = value


    def getFile(self, entry):
        def getfile():
            filename = tkFileDialog.askopenfilename()
            entry.insert(0, filename)
        return getfile

    def createWidgetsTest(self):
        self.label = Label(
            self,
            text='hahaha',
            font=(
                'Arial',
                20),
            bg='red',
            width=15,
            height=3)
        self.label.pack(side=LEFT)
        self.scale = Scale(
            self,
            from_=10,
            to=40,
            orient=HORIZONTAL,
            command=self.resize)
        self.scale.pack()

        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

        frmL = Frame(self.master)
        Label(frmL, text='厚德', font=('Arial', 15)).pack(side=TOP)
        Label(frmL, text='博学', font=('Arial', 15)).pack(side=TOP)
        frmL.pack(side=LEFT)

        frmR = Frame(self.master)
        Label(frmR, text='敬业', font=('Arial', 15)).pack(side=TOP)
        Label(frmR, text='乐群', font=('Arial', 15)).pack(side=TOP)
        frmR.pack(side=RIGHT)

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'hello, %s' % name)

    def resize(self, ev=None):
        self.label.config(font='Arial %d' % self.scale.get())
