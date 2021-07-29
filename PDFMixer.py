import PyPDF2
import argparse
from os import path
import sys

def printError(msg):
	parser.print_usage()
	print(msg)
	sys.exit()

# Options
parser = argparse.ArgumentParser(
    description="Merge odd and reversed even pages into a pdf file")
parser.add_argument("-o", "--odd", metavar='<pdf file>',
                    help='pdf file with odd pages', required=True)
parser.add_argument("-e", "--even", metavar='<pdf file>',
                    help='pdf file with reversed even pages (default: merged.pdf)', required=True)
parser.add_argument("pdf", metavar='<pdf file>', default="merged.pdf",
                    help='output pdf file', nargs='?')
args = parser.parse_args()

# Check if files exist
if not path.isfile(args.odd):
	printError(f"Error: {args.odd} does not exist")
if not path.isfile(args.even):
	printError(f"Error: {args.even} does not exist")

# Add .pdf to outpuf file if omitted
if not args.pdf.endswith(".pdf"):
    output = "".join([args.pdf, ".pdf"])
else:
    output = args.pdf

# Create file objects
pdfFileObj_1 = open(args.odd, 'rb')
pdfFileObj_2 = open(args.even, 'rb')
pdfWriter = PyPDF2.PdfFileWriter()

# Check if input files are pdf and can be opened
try:
    pdfReader_impair = PyPDF2.PdfFileReader(pdfFileObj_1)
    pdfReader_pair = PyPDF2.PdfFileReader(pdfFileObj_2)
except:
	printError("Error: PDF files cannot be read")

# Check if input files have the same number of pages
nbPages = pdfReader_pair.numPages
if not nbPages == pdfReader_impair.numPages:
	printError("Error: Odd and even pdf files must have the same number of pages")

# Merge input pdf files
for page in range(nbPages):
    pageObj = pdfReader_impair.getPage(page)
    pdfWriter.addPage(pageObj)
    pageObj = pdfReader_pair.getPage(nbPages - page - 1)
    pdfWriter.addPage(pageObj)

# Write output pdf
newFile = open(output, 'wb')
pdfWriter.write(newFile)

# Close file objects
pdfFileObj_1.close()
pdfFileObj_2.close()
newFile.close()
