from PyPDF2 import PdfMerger

get1 = input("Enter the path of the first PDF file: ")
get2 = input("Enter the path of the second PDF file: ")
get3 = input("Enter the Name of the merged PDF file (with .pdf extension): ")

allpdf = [get1, get2]

marger = PdfMerger()

for newpdf in allpdf:
    marger.append(newpdf)
marger.write(get3)
marger.close()