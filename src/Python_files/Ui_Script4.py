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

def number(text):
    text = text.upper()
    res=text.split()
    aadhar_number=''
    '''if 'Male' or 'Female' in res:
        lst = res[-3:]
        print(lst)'''
    i=0
    fres=0
    cou=len(res)
    for i in range(cou):
        if((res[i]=='MALE' or res[i]=='FEMALE') and fres==0):
            fres=1
        if(fres==1 and res[i].isdigit() and len(aadhar_number)<15):
            aadhar_number = aadhar_number + res[i] + ' '
    
    if len(aadhar_number) >= 13:
        print ("Aadhar Number : "+aadhar_number)
        return ("Aadhar Number : "+aadhar_number)
    else:
         print("Aadhar number not read")
         return ("Aadhar number not read")
    
