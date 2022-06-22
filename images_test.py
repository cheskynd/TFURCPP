import tkinter
import _tkinter
import tkinter

win = tkinter.Tk()
win.title("GIF TEST")

files = ["lion.png", "newyork.png"]
photos = [tkinter.PhotoImage(file=x) for x in files]
label = tkinter.Label()
label.photos = photos
label.counter = 0


def next_pic():
    label['image'] = label.photos[label.counter % len(label.photos)]
    label.after(1000, next_pic)
    label.counter += 1


label.pack()
next_pic()

win.mainloop()
