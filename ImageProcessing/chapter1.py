import cv2
import numpy as np
import tkinter as tk

img_array = ["Resources/Elohim.JPG", "Resources/Egy hangon.JPG"]

top = tk.Tk()
top.geometry("640x480")
index = 0
low_blue_arr = [110, 200, 0]
high_blue_arr = [255, 255, 255]
isItThreshold = False


def show_img(this_img):
    hsv = cv2.cvtColor(this_img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array(low_blue_arr)
    upper_blue = np.array(high_blue_arr)

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    if not isItThreshold:
        res = cv2.bitwise_and(this_img, this_img, mask=mask)
    else:
        thresh = cv2.adaptiveThreshold(mask, 120, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        res = cv2.bitwise_and(this_img, this_img, mask=thresh)

    title = img_array[index][10:]

    cv2.imshow(title, this_img)
    cv2.imshow('res', res)
    return


def next_image():
    cv2.destroyAllWindows()
    global index
    _thisImg = cv2.imread(img_array[index])
    if len(img_array)-1 > index:
        index += 1
    show_img(_thisImg)

    return


def prev_image():
    cv2.destroyAllWindows()
    global index
    _thisImg = cv2.imread(img_array[index])
    if index > 0:
        index -= 1

    show_img(_thisImg)
    return


def change():
    global isItThreshold
    cv2.destroyAllWindows()
    _thisImg = cv2.imread(img_array[index])
    if isItThreshold:
        isItThreshold = False
        show_img(_thisImg)
        return
    isItThreshold = True
    show_img(_thisImg)


p = tk.Button(top, text="Previous image", command=prev_image)
b = tk.Button(top, text="Next image", command=next_image)
c = tk.Button(top, text="Change to threshold", command=change)
b.pack()
p.pack()
c.pack()
top.mainloop()
