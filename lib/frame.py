# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox
import Tkinter
import tkFileDialog


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # frame_l = Frame(self.master)
        Label(self, text='产品报价明细:', font=(
            'Arial', 15)).grid(row=0, column=0)
        Label(self, text='店铺销售明细:', font=(
            'Arial', 15)).grid(row=1, column=0)
        Label(self, text='快递单号明细:', font=(
            'Arial', 15)).grid(row=2, column=0)
        Label(self, text='快递费用明细:', font=(
            'Arial', 15)).grid(row=3,column=0)
        self.entry1 = Entry(self)
        self.entry2 = Entry(self)
        self.entry3 = Entry(self)
        self.entry4 = Entry(self)
        self.entry1.grid(row=0, column=2)
        self.entry2.grid(row=1, column=2)
        self.entry3.grid(row=2, column=2)
        self.entry4.grid(row=3, column=2)
        self.button1 = Button(self, text=u'点击选择文件', command=self.getFile(self.entry1))
        self.button2 = Button(self, text=u'点击选择文件', command=self.getFile(self.entry2))
        self.button3 = Button(self, text=u'点击选择文件', command=self.getFile(self.entry3))
        self.button4 = Button(self, text=u'点击选择文件', command=self.getFile(self.entry4))
        self.button1.grid(row=0, column=3)
        self.button2.grid(row=1, column=3)
        self.button3.grid(row=2, column=3)
        self.button4.grid(row=3, column=3)



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

        frm_L = Frame(self.master)
        Label(frm_L, text='厚德', font=('Arial', 15)).pack(side=TOP)
        Label(frm_L, text='博学', font=('Arial', 15)).pack(side=TOP)
        frm_L.pack(side=LEFT)

        frm_R = Frame(self.master)
        Label(frm_R, text='敬业', font=('Arial', 15)).pack(side=TOP)
        Label(frm_R, text='乐群', font=('Arial', 15)).pack(side=TOP)
        frm_R.pack(side=RIGHT)

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'hello, %s' % name)

    def resize(self, ev=None):
        self.label.config(font='Arial %d' % self.scale.get())
