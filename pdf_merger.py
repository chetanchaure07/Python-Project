from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["First_Pdf_Location", "Second_Pdf_Location", "Till_N_Pdf_Location"]:
    merger.append(pdf)

merger.write("Merged-pdf.pdf")
merger.close()