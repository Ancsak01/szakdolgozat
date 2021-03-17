import rdflib as rdf
import pytesseract
import cv2


class ReadImage:

    def __init__(self):
        pass

    def read_file(self, pic, name):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        alter = pytesseract.image_to_string(pic, lang='hun', config='--psm 6')
        hImg, wImg, _ = pic.shape
        boxes = pytesseract.image_to_boxes(pic)
        for b in boxes.splitlines():
            b = b.split(' ')
            print(b)
            x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(pic, (x, hImg-y), (w, hImg-h), (0, 0, 255), 3)
            cv2.putText(pic, b[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50 ,255), 2)

        cv2.imshow('ASD', pic)
        # print(alter)
        # names = name.split(".")
        # f = open("../outputTexts/"+names[0]+".txt", "x")
        # f.write(alter)
        # f.close()

    def encode(self, text):
        print(text)

