# EXTRAIRE LE TEXTE DES FICHIERS PDF
from PyPDF2 import PdfFileWriter, PdfFileReader

f = open("recap.pdf", "rb")
reader = PdfFileReader(f)

page0 = reader.getPage(1)
texte = page0.extractText()

texte = texte.replace("Ò", '"').replace("‘", "è").replace("‹", "à").replace("”", "é").replace("Õ", "'").replace("’", "ê")

f.close()


print(texte)




