
# -*- coding: utf-8 -*-


import tkinter
import message


def power():
    WIDTH_HEIGHT = '400x299'
    WINDOW_POSITION = '+550+280'
    
    power = tkinter.Toplevel(message.about)
    power.title('Power')
    power.geometry(WIDTH_HEIGHT)
    power.geometry(WINDOW_POSITION)
    power.resizable(False, False)
    power.transient(message.about)
    power.iconbitmap('./iphoto_icon.ico')

    background = tkinter.Label(power, width=400, 
                               height=299, bg='#d3d3d3')
    background.pack()

    title = tkinter.Label(power, text='Support',  
                          fg='black', bg='#d3d3d3',
                          font=('微软雅黑', 20))
    title.place(x=140, y=40)

    information = tkinter.Label(power, text=
                                'Designed by Photos Support in China'
                                +'\n' + 
                                'Copyright ©2019.Python.org'
                                + '\n' + 
                                'Power by Python', 
                                fg='black', bg='#d3d3d3',
                                font=('微软雅黑', 12))

    information.place(x=50, y=170)
 