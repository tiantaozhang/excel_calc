# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox
import Tkinter

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.label = Label(self, text='hahaha', font=('Arial', 20), bg='red', width=15, height=3)
        self.label.pack(side=LEFT)
        self.scale = Scale(self, from_=10,to=40, orient=HORIZONTAL, command=self.resize)
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

    def resize(self,ev=None):
        self.label.config(font='Arial %d' % self.scale.get())