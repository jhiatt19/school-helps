To set up computer you need to download/install 3 packages:

1) Python -> https://www.python.org/downloads
2) Tesseract OCR -> https://github.com/UB-Mannheim/tesseract/wiki
3) pdf2image/Poppler -> https://github.com/oschwartz10612/poppler-windows

You will need to go in and add the Tesseract OCR and pdf2image/Poppler to the PATH environment variables. To do this ask your favorite AI for the steps to do this on your specific operating system.

To run the program:
Get into the folder that has the files saved.
call script "path to pdf" "path to .txt file"

For example: python pdf-splitter "/readthistext.pdf" "/tothisplace.txt" 

Pdf-splitter takes the .pdf and turns it into a .txt
Pdf-halfer takes a pdf that has 2 pages like a book and splits it into 2 different .pdf's and then you can use pdf-splitter on it.
