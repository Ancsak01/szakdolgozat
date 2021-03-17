from __future__ import print_function
from tkinter import HORIZONTAL

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display

import cv2
import numpy as np
import tkinter as tk
import ReadImage

img_array = ["../samples/Elohim.JPG", "../samples/Egy hangon.JPG"]

top = tk.Tk()
r = ReadImage.ReadImage()

top.geometry("640x480")
index = 0
low_blue_arr = [50, 195, 0]
high_blue_arr = [123, 255, 255]
isItThreshold = False


def show_img(this_img, imname):
    hsv = cv2.cvtColor(this_img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array(low_blue_arr)
    upper_blue = np.array(high_blue_arr)

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    if not isItThreshold:
        res = cv2.bitwise_or(this_img, this_img, mask=mask)
    else:
        thresh = cv2.adaptiveThreshold(mask, 120, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        res = cv2.bitwise_and(this_img, this_img, mask=thresh)

    title = img_array[index][11:]

    cv2.imshow(title, this_img)
    cv2.imshow('res', res)
    r.read_file(res, title)
    return


def next_image():
    cv2.destroyAllWindows()
    global index
    if len(img_array)-1 > index:
        index += 1
    _thisImg = cv2.imread(img_array[index])
    show_img(_thisImg, img_array[index])

    return


def prev_image():
    cv2.destroyAllWindows()
    global index
    if index > 0:
        index -= 1
    _thisImg = cv2.imread(img_array[index])
    show_img(_thisImg, img_array[index])
    return


def change():
    global isItThreshold
    cv2.destroyAllWindows()
    _thisImg = cv2.imread(img_array[index])
    if isItThreshold:
        isItThreshold = False
        show_img(_thisImg, img_array[index])
        return
    isItThreshold = True
    show_img(_thisImg, img_array[index])

a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))

# p = tk.Button(top, text="Previous image", command=prev_image)
# b = tk.Button(top, text="Next image", command=next_image)
# c = tk.Button(top, text="Change to threshold", command=change)
# lab_l_r = tk.Label(top, text="Low Red:")
# drag_low_red = tk.Scale(top, from_=0, to=255, orient=HORIZONTAL)
# lab_l_g = tk.Label(top, text="Low Green:")
# drag_low_green = tk.Scale(top, from_=0, to=255, orient=HORIZONTAL)
# lab_l_b = tk.Label(top, text="Low Blue:")
# drag_low_blue = tk.Scale(top, from_=0, to=255, orient=HORIZONTAL)
# lab_h_r = tk.Label(top, text="High Red:")
# drag_high_red = tk.Scale(top, from_=0, to=255, orient=HORIZONTAL)
# lab_h_g = tk.Label(top, text="High Green:")
# drag_high_green = tk.Scale(top, from_=0, to=255, orient=HORIZONTAL)
# lab_h_b = tk.Label(top, text="High Blue:")
# drag_high_blue = tk.Scale(top, from_=0, to=255, orient=HORIZONTAL)
# b.pack()
# p.pack()
# c.pack()
# lab_l_r.pack()
# drag_low_red.pack()
# lab_l_g.pack()
# drag_low_green.pack()
# lab_l_b.pack()
# drag_low_blue.pack()
# lab_h_r.pack()
# drag_high_red.pack()
# lab_h_g.pack()
# drag_high_green.pack()
# lab_h_b.pack()
# drag_high_blue.pack()
# top.mainloop()
