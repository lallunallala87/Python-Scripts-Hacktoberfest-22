import os
from PyPDF2 import PdfFileMerger

output_file = "merged.pdf"

pdfs_list = [file for file in os.listdir() if file.endswith(".pdf")]
pdfs_list = sorted(pdfs_list, key=lambda file: os.path.splitext(file)[0])

merger = PdfFileMerger()
for pdf in pdfs_list:
    merger.append(pdf)

merger.write(output_file)
merger.close()