import PyPDF2
import argparse
from os import path
import sys

# Options
parser = argparse.ArgumentParser(
    description="Merge odd and reversed even pages into a pdf file")
parser.add_argument("-o", "--odd")
parser.add_argument("-e", "--even")
parser.add_argument("-p", "--pdf", default="merged.pdf",
                    help='output pdf file')
args = parser.parse_args()

if not path.isfile(args.odd):
	parser.print_usage()
	print("Error: args.odd does not exist")
	sys.exit()
if not path.isfile(args.even):
	parser.print_usage()
	print("Error: args.even does not exist")
	sys.exit()

pdfFileObj_1 = open(args.odd, 'rb')
pdfFileObj_2 = open(args.even, 'rb')
pdfWriter = PyPDF2.PdfFileWriter()

pdfReader_impair = PyPDF2.PdfFileReader(pdfFileObj_1)
pdfReader_pair = PyPDF2.PdfFileReader(pdfFileObj_2)

nbPages = pdfReader_pair.numPages
print(f"TOTAL: {nbPages}")

for page in range(nbPages):
    print(f"Current: {page}")
    pageObj = pdfReader_impair.getPage(page)
    pdfWriter.addPage(pageObj)
    pageObj = pdfReader_pair.getPage(nbPages - page - 1)
    pdfWriter.addPage(pageObj)

newFile = open(args.pdf, 'wb')
pdfWriter.write(newFile)
pdfFileObj_1.close()
pdfFileObj_2.close()
newFile.close()
