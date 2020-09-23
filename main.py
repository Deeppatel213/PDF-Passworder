import PyPDF2

a=PyPDF2.PdfFileReader(r'G:\DEEP\DEEP\collage\TT.pdf')
b=PyPDF2.PdfFileWriter()

for i in range(a.numPages):
    b.addPage(a.getPage(i))

password="22122001"
b.encrypt(password)

with open('G:\DEEP\DEEP\collage\\New TT.pdf','wb') as f:
    b.write(f)
    f.close()