import sys 
import os
import cv2
import os.path
import re
import numpy as np
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(path):
     pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Qbx-sys2/AppData/Local/Tesseract-OCR/tesseract.exe' 
     img = cv2.imread("C:/Users/Qbx-sys2/AppData/Local/Programs/Python/Python36/"+path+".jpg", cv2.IMREAD_UNCHANGED)

     # resize image
     resized = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
     img = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
     return pytesseract.image_to_string(img, lang='eng')
     #cv2.imshow("Resized image", resized)
     #cv2.imshow("Resized image", img)
     #print(text)
     #return text
     
     
#ocr_core()
