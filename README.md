# PDFMixer

## What

This script merges 2 pdf in one.

The 2 input pdf must be:

* odd: contains all odd pages in numerical order
* even: contains all even pages in reversed numerical order

It is written in Python 3

## Why

Case: when scanned with a printer that can handle multiple pages

## Requirements

```bash
pip install -r requirements.txt
```

OR

```bash
pip install PyPDF2
```

## --help

```bash
usage: PDFMixer.py [-h] -o <pdf file> -e <pdf file> [<pdf file>]

Merge odd and reversed even pages into a pdf file

positional arguments:
  <pdf file>            output pdf file

optional arguments:
  -h, --help            show this help message and exit
  -o <pdf file>, --odd <pdf file>
                        pdf file with odd pages
  -e <pdf file>, --even <pdf file>
                        pdf file with reversed even pages (default: merged.pdf)
```

### Exemple

Call the script with the following command:

```bash
python3 PDFMixer.py -o odd.pdf -e even.pdf merged.pdf
```
