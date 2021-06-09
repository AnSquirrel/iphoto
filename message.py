
# -*- coding: utf-8 -*-


import tkinter.messagebox
import power


class MessageBox(object):
    def __init__(self, message=tkinter.messagebox):
        self.message = message

    def aboutPhotos(self):       
        self.message.showinfo(
            'About Mojave', 
            '            Mojave' 
            + '\n' + '\n' + '\n' +
            'Copyright (C)2001-2019.Python.org' 
            + '\n' + 
            '       Photos Version 1.0.0')

    def aboutPhotos(self):
        global about

        WIDTH_HEIGHT = '290x140'
        WINDOW_POSITION = '+600+400'

        about = tkinter.Toplevel()
        about.title('about')
        about.geometry(WIDTH_HEIGHT)
        about.geometry(WINDOW_POSITION)
        about.resizable(False, False)
        about.transient()
        about.iconbitmap('./iphoto_icon.ico')

        background = tkinter.Label(about, width=290, height=140, bg='#d3d3d3')
        background.pack()

        title = tkinter.Label(about, text='Photos', fg='black', bg='#d3d3d3', font=('Arial', 20))
        title.place(x=105, y=15)

        information = tkinter.Label(about, 
            text='Copyright ©2019.Python.org'
            + '\n' + 
            'Photos Version 1.0.0',  
            fg='black', bg='#d3d3d3', font=('Arial', 10))
        information.place(x=50, y=80)

        powerbutton = tkinter.Button(about, text='Power', 
            width=6, height=1 , fg='black', bg='#d3d3d3', 
            command=power.power, font=('Arial', 8))

        powerbutton.place(x=40, y=23)

    def printMessage(self):
        self.message.showerror('Photos Print', 'Unconnect printer     ')

    def exitMessage(self):
        _exit = self.message.askokcancel('Photos Exit', 'Exit Photos')
        if _exit == True:
            quit()

MessageBox = MessageBox()
