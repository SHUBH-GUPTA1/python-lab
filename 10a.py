# from PyPDF2 import PdfReader,PdfWriter
# num=int(input("enter the page number to combine"))
# pdf1=open("DAA MOdule1.pdf",'rb')
# pdf2=open("DAA MOdule2.pdf",'rb')

# pdf_writer=PdfWriter()

# pdf1_reader=PdfReader(pdf1)
# page=pdf1_reader.pages[num-1]
# pdf_writer.add_page(page)

# pdf2_reader=PdfReader(pdf2)
# page=pdf2_reader.pages[num-1]
# pdf_writer.add_page(page)

# with open('output.pdf','wb') as output:
#     pdf_writer.write(output)




from PyPDF2 import PdfReader,PdfWriter

num=int(input("enter page no. to combine"))
pdf1=open("DAA1.pdf",'rb')
pdf2=open("DAA2.pdf",'rb')
pdf_writer=PdfWriter()

pdf1_reader=PdfReader(pdf1)
page=pdf1_reader.pages[num-1]
pdf_writer.add_page(page)

pdf2_reader=PdfReader(pdf2)
page=pdf2_reader.pages[num-1]
pdf_writer.add_page(page)

with open('output.pdf','wb') as output:
    pdf_writer.write(output)
