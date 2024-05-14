import cv2
import tkinter as tk
from tkinter import *
import customtkinter

from tkinter import filedialog
from tkinter.filedialog import askopenfile
import time
import numpy as np
from PIL import ImageTk,Image
import sys
if sys.version_info[0] < 3:
   import Tkinter as Tk
else:
   import tkinter as Tk


def browse_file():

    fname = filedialog.askopenfilename(filetypes = (("All files", "*.type"), ("All files", "*")))
    print(fname)
    cap = cv2.VideoCapture(fname)
    car_cascade = cv2.CascadeClassifier(r'C:\Users\Muhammad Hassan\Desktop\Desktop Kachra\CV project\hassan_haarcascade_car.xml')

    while True:
        ret, frames = cap.read()
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 9)
    # if str(np.array(cars).shape[0]) == '1':
    #     i += 1
    #     continue
        for (x,y,w,h) in cars:
         plate = frames[y:y + h, x:x + w]
         cv2.rectangle(frames,(x,y),(x +w, y +h) ,(51 ,51,255),2)
         cv2.rectangle(frames, (x, y - 40), (x + w, y), (51,51,255), -2)
         cv2.putText(frames, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
         cv2.imshow('car',plate)

    # lab1 = "Car Count: " + str(i)
    # cv2.putText(frames, lab1, (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (147, 20, 255), 3)
        frames = cv2.resize(frames,(600,400))
        cv2.imshow('Car Detection System', frames)
    # cv2.resizeWindow('Car Detection System', 600, 600)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
         break
    cv2.destroyAllWindows()

root = Tk.Tk()
root.wm_title("Car Detection System")
root.geometry('300x400')
broButton = Tk.Button(master = root, text = 'Pick Video File', width = 20, command=browse_file)
broButton.place(relx=0.5, rely=0.5,anchor=CENTER)
qButton = Tk.Button(master = root, text = 'Exit', width = 20, command=root.quit)
qButton.place(relx=0.5, rely=0.9,anchor=CENTER)
Tk.mainloop()