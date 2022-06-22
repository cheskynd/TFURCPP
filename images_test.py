import tkinter
import _tkinter
import tkinter
from tkinter import *


win = tkinter.Tk()
win.title("GIF TEST")

files = ["lion.png", "newyork.png"]
photos = [tkinter.PhotoImage(file=x) for x in files]
label = tkinter.Label()
label.photos = photos
label.counter = 0


def next_pic():
    label['image'] = label.photos[label.counter % len(label.photos)]
    label.after(2000, next_pic)
    label.counter += 1


label.pack()
next_pic()

win.mainloop()


#################################################################################3
import time
import random
#
# def move_up(event):
#     label.place(x = label.winfo_x(), y=label.winfo_y()-10)
# def move_down(event):
#     label.place(x = label.winfo_x(), y=label.winfo_y()+10)
# def move_left(event):
#     label.place(x = label.winfo_x()-10, y=label.winfo_y())
# def move_right(event):
#     label.place(x = label.winfo_x()+10, y=label.winfo_y())
#
# window = Tk()
# window.geometry("500x500")
#
# window.bind("<w>", move_up)
# window.bind("<s>", move_down)
# window.bind("<a>", move_left)
# window.bind("<d>", move_right)
# window.bind("<Up>", move_up)
# window.bind("<Down>", move_down)
# window.bind("<Left>", move_left)
# window.bind("<Right>", move_right)
#
# images = ['This Ramen Is My Girlfriend.png']
# for i in range(len(images)):
#     myimage = PhotoImage(file=images[i])
#     label = Label(window, image=myimage)
#     label.place(x=0, y=0)
#     time.sleep(5)
#
#
# window.mainloop()
#########################################################33
def move_up(event):
    canvas.move(myimage,0,-10)
def move_down(event):
    canvas.move(myimage,0,+10)
def move_left(event):
    canvas.move(myimage,-10,0)
def move_right(event):
    canvas.move(myimage,+10,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoimage = PhotoImage(file='lion.png')
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

window.mainloop()
