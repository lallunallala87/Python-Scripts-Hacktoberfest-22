import PyPDF2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title = "Select Pdf to start with") 

pdf = open(file_path, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)

pages = pdfReader.numPages
s=""
numbering = input("Print page numbers? (Y/n) ").lower()
for pg in range(pages):
    if numbering=="y":
        s += "Page " + str(pg+1) + ":\n\n"
    pageObj = pdfReader.getPage(pg)
    texts = pageObj.extractText()
    s += texts + "\n\n\n"

folder_selected = filedialog.askdirectory(title = "Select directory to save .txt file")         # Select directory to store text file

name = input("Enter name for text file: ")
name = folder_selected + "/" + name + ".txt"

with open(name, "w") as file_obj:
    file_obj.write(s)
print("PDF converted succesfully and stored => ", name)
