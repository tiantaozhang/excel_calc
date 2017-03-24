# -*- conding: utf-8 -*-

# calculator the result
from lib.frame import Application
# from FileDialog import  *
# import tkFileDialog

def centerWindow(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    # print(size)
    root.geometry(size)

if __name__ == '__main__':
    app = Application()
    app.master.title('muscle professional')
    # app.master.geometry('880x360')
    centerWindow(app.master, 880, 360)
    app.master.resizable(width=False, height=False)
    app.mainloop()

