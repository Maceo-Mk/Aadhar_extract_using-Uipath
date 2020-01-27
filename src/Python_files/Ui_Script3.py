import pytesseract
from PIL import Image
import datetime
import cv2
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import os.path
import re
import numpy as np
def Year(text):
    res=text.split()
    if 'Year of Birth' in text:
        inde=res.index('Birth')#>=——
        yob=''
        res[inde+2].isalpha()
        yob= res[inde+2] 
        print("Year of Birth:  " + yob)
        return("Year of Birth:  " + yob)
    else:
        p = re.compile('\d+/\d+/\d+')
        if (p.findall(text)):
            dates=p.findall(text)
        if len(dates)>0 and len(dates[0])>1:
           print("Date of birth : "+ str(dates[0]))
           return("Date of birth : "+ str(dates[0]))
