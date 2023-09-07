import PyPDF2

pdfile=["1.pdf","2.pdf"]
merger=PyPDF2.PdfMerger()
merger = PyPDF2. PdfMerger ()
for filename in pdfile:
    pdffile = open (filename, 'rb')
    pdfReader = PyPDF2.PdfReader (pdfile)
    merger. append (pdfReader)
pdffile.close()
merger.write('merged.pdf')