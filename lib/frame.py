# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox
import Tkinter
import tkFileDialog


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.e1 = StringVar()
        self.e2 = StringVar()
        self.e3 = StringVar()
        self.e4 = StringVar()
        self.eResult = StringVar()
        self.createWidgets()

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
        print self.e1.get(),self.e2,self.e3,self.e4
        self.eResult.set('/here/we/are')


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
