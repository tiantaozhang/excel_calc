# -*- conding: utf-8 -*-

# calculator the result
from lib.frame import Application
# from FileDialog import  *
import tkFileDialog

if __name__ == '__main__':
    app = Application()
    app.master.title('Hello world!')
    app.master.geometry('400x400')
    filename = tkFileDialog.askopenfilename()
    print filename
    app.mainloop()

