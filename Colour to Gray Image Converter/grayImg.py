import cv2
import imutils
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

img=cv2.imread(file_path)    # reads image
new_path = input("Do you want to save image in same path? (Y/n) ").lower()

if new_path=="n":
    loc = input("Enter new path to save image: ")       # saving path to store at desired location
print(f"Saving image at {loc}")

grayImg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            # recoloring image to gray
cv2.imwrite(os.path.join(loc, f"gray-{file}"), grayImg)  # saving gray image
