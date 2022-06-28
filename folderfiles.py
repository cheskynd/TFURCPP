#import cv2
import glob
import numpy as np
import tkinter as tk
from PIL import ImageTk
from tkinter import *
import ctypes
import tkinter
from PIL import Image, ImageTk

#shows transperancy with open CV
path = cv2.imread("blue.jpg")
bgra = cv2.cvtColor(path, cv2.COLOR_BGR2BGRA)
#transperancy number, if its 0 then it will be fully transparent
bgra[...,3] = 127
cv2.imwrite('result.png',bgra)
t= Image.open('result.png')
t.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

#shows transperancy with tkinter

# root = tk.Tk()
# # use opacity alpha values from 0.0 to 1.0
# # opacity/tranparency applies to image and frame
# root.wm_attributes('-alpha', 0.3)
# # use a GIF image you have in the working directory
# # or give full path
# photo = tk.PhotoImage(file="lion.png")
# tk.Label(root, image=photo).pack()
# root.mainloop()



#using cv to run a cycle of images with resizing
path = glob.glob("C:\Users\landerosn\Pictures\Marvel*.jpg")
images1 = []
for file in path:
    img= cv2.imread(file)
    img= cv2.resize(img, (200,200))
    images1.append(img)
    num_rows, num_cols = img.shape[:2]
    translate = np.float32([[1,0,70],[0,1,110]])
    imgtran = cv2.warpAffine(img, translate, (num_cols + 70, num_rows +110))
    translate = np.float32([[1, 0, -30], [0,1,-50]])
    imgtran = cv2.warpAffine(imgtran, translate, (num_cols + 70 + 30, num_rows +110 +50))
    cv2.namedWindow('translation', cv2.WINDOW_NORMAL)
    cv2.imshow("translation", imgtran)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

##################################################################333
#resizing image through TK
# root = Tk()
#
# # Read the Image
# image = Image.open("newyork.png")
#
# # Resize the image using resize() method
# resize_image = image.resize((400, 400))
#
# img = ImageTk.PhotoImage(resize_image)
#
# # create label and add resize image
# label1 = Label(image=img)
# label1.image = img
# label1.pack()
#
# # Execute Tkinter
# root.mainloop()


###########################################################
# root = Tk()
#
# # Read the Image
# image = Image.open("newyork.png")
#
# # Resize the image using resize() method
# resize_image = image.resize((400, 400))
#
# img = ImageTk.PhotoImage(resize_image)
#
# # create label and add resize image
# label1 = Label(image=img)
# label1.image = img
# label1.pack()
#
# # Execute Tkinter
# root.mainloop()
###########################################################33
# win = tkinter.Tk()
# win.title("GIF TEST")
#
# files = ["lion.png", "newyork.png"]
# photos = [tkinter.PhotoImage(file=x) for x in files]
# label = tkinter.Label()
# label.photos = photos
# label.counter = 0
#
# def next_pic():
#     label['image'] = label.photos[label.counter % len(label.photos)]
#     label.after(1000, next_pic)
#     label.counter += 1
# label.pack()
# next_pic()
#
# win.mainloop()
################################################################
#cycle of pics
import PIL
import os
# import os.path
# from PIL import Image
#
# f = r'C:\Users\landerosn\Pictures\Marvel'
# imgs = []
# for file in os.listdir(f):
#     f_img = f+"/"+file
#     img = Image.open(f_img)
#     img = img.resize((400,400))
#     img.save(f_img)
##############################################################
## integration of resizing and transperancy

# root = tk.Tk()
# root.wm_attributes('-alpha', 0.3)
#
# image = Image.open("newyork.png")
# resize_image = image.resize((400, 400))
# img = ImageTk.PhotoImage(resize_image)
# label1 = Label(image=img)
# label1.image = img
# label1.pack()
# root.mainloop()

images = ['newyork.png', 'lion.png']
for image in images:
        img = Image.open(image)
        img.show()



