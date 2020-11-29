import rdflib as rdf
import pytesseract

class ReadImage:

    def __init__(self):
        pass

    def read_file(self, pic, name):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\tryba\AppData\Local\Tesseract-OCR\tesseract.exe'
        alter = pytesseract.image_to_string(pic)
        names = name.split(".")
        f = open(names[0]+".txt", "x")
        f.write(alter)
        f.close()
