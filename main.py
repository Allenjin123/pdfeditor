import os
from PyPDF2 import PdfFileReader, PdfFileWriter

import glob
from PyPDF2 import PdfFileWriter, PdfFileReader

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}_page_{}.pdf'.format(
            fname, page + 1)
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)


def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

def extrat(input_path, output_path,start_page, end_page):
    #fname = os.path.splitext(os.path.basename(input_path))[0]
    pdf = PdfFileReader(input_path)
    pdf_writer = PdfFileWriter()
    for page in range(start_page,end_page+1,1):
        pdf_writer.addPage(pdf.getPage(page))
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

def del_file(path):
    for root,dirs,files in os.walk(path):
        for name in files:
            if 'Everyday Writer with Exercises 6th ed-TA' in name:
                os.remove(os.path.join(root,name))
                print('Delete files: ',os.path.join(root,name))

# if __name__=='__main__':
#     path=r'C:\Users\lenovo\Desktop\pdfdivider'
#     del_file(path)
# paths = glob.glob('w9_*.pdf')
# paths.sort()
# merger('pdf_merger.pdf', paths)

path = 'VY200-S5.pdf'
pdf_splitter(path)
# extrat(path,'test.pdf',231+34+7,239+34+7)