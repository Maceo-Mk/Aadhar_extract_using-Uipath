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
def is_aadhar_card(text):
               text = text.upper()
              # print(text)
               res=text.split()
              # print(res)
               dates={}           
               if 'GOVERNMENT OF INDIA' in text:
                   print ("Aadhar card is valid and the details are below:")
                   index=res.index('INDIA')#>=——
                   name=''
                   if (res[index+3].isalpha()):
                     # print(res[index+3])
                      name= res[index+4] + " " + res[index+5] + " " + res[index+6]
                   else :
                      name= res[index+4] + " " + res[index+5] + " " + res[index+6]
               else:
                    name=res[2] + " " + res[3]
               if len(name)>1:
                   print("Name :  " + name)
                   return("Name :  " + name)
               else:
                    print("Name not read")
                    return ("Name not read")
            
