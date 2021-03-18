import csv
import os
import re
import cv2
import pytesseract
import numpy as np
from pytesseract import Output

# pytesseract.pytesseract.tesseract_cmd = r"C:\Users\AvelinaK\Documents\Machine Learning\tesseract.exe"

#Configs for local execution
# TesserOCR_exe_file = 'tesseract.exe'
# site_packages_path = 'venv\Lib\site-packages'
# CURR_DIRECTORY = os.getcwd()
# path_for_sitePackages = os.path.join(os.getcwd(),site_packages_path)
# pytesseract.pytesseract.tesseract_cmd = os.path.join(path_for_sitePackages,TesserOCR_exe_file)

pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'

def extract_PanCard_Fields(path):
    img = cv2.imread(path)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    keys = list(d.keys())

    dob_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
    pan_number_pattern = '[A-Z]{5}[0-9]{4}[A-Z]{1}'

    matched_text = {'DOB':'','PAN_Number':''}
    n_boxes = len(d['text'])
    print(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            if re.match(dob_pattern, d['text'][i]):
                matched_text['DOB'] = d['text'][i]
                print("DOB: "+ d['text'][i]+ "\n")
            if re.match(pan_number_pattern, d['text'][i]):
                matched_text['PAN_Number'] = d['text'][i]
                print("PAN Number: "+ d['text'][i]+ "\n")
    return matched_text

def extract_DriverLicense_Fields(path):
    img = cv2.imread(path)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    keys = list(d.keys())

   # drivingLicense_pattern = '^(([A-Z]{2}[0-9]{2})( )|([A-Z]{2}-[0-9]{2}))((19|20)[0-9][0-9])[0-9]{7}$'

    matched_text = {'Licence_No':'','DOB':'','Name':'','Valid_Till':''}
    # n_boxes = len(d['text'])
    # print(d['text'])
    filter_characters = filter(lambda x: (x != ":"), d['text'])
    d['text'] = list(filter_characters)
    n_boxes = len(d['text'])
    print(d['text'])

    for i in range(n_boxes):
        #if int(d['conf'][i]) > 60:
        if (d['text'][i] == 'DL' or d['text'][i] == 'Licence'):
            if (d['text'][i+1] == 'No' or d['text'][i+1] == 'No.'):
                matched_text['Licence_No'] = d['text'][i+2]
                print("Licence No: "+ d['text'][i+2]+ "\n")
        if (d['text'][i] == 'Name'):
            matched_text['Name'] = d['text'][i+1]+' '+d['text'][i+2]+' '+d['text'][i+3]
            print("Name: "+ d['text'][i+1]+''+d['text'][i+2]+''+d['text'][i+3]+ "\n")
        if (d['text'][i] == 'DOB' or d['text'][i] == 'DOB:'):
            matched_text['DOB'] = d['text'][i + 1]
            print("DOB: " + d['text'][i + 1] +"\n")
        if (d['text'][i] == 'Valid'):
            if (d['text'][i+1] == 'Till'):
                matched_text['Valid_Till'] = d['text'][i+2]
                print("Valid Till: "+ d['text'][i+2]+ "\n")
    return matched_text

def extract_AadharCard_Fields(path):
    img = cv2.imread(path)

    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    keys = list(d.keys())

    matched_text = {'Aadhar_No':'','DOB':'','Name':'','Gender':''}
    filter_characters = filter(lambda x: (x != ":"), d['text'])
    d['text'] = list(filter_characters)
    n_boxes = len(d['text'])
    print(d['text'])

    for i in range(n_boxes):
        if (d['text'][i] == 'Name' or d['text'][i] == 'Name:'):
            matched_text['Name'] = d['text'][i+1]+' '+d['text'][i+2]+' '+d['text'][i+3]
            print("Name: "+ d['text'][i+1]+''+d['text'][i+2]+''+d['text'][i+3]+ "\n")
        if (d['text'][i] == 'DOB' or d['text'][i] == 'DOB:'):
            matched_text['DOB'] = d['text'][i + 1]
            print("DOB: " + d['text'][i + 1] +"\n")
        if (d['text'][i] == 'Male' or d['text'][i] == 'Female'):
            matched_text['Gender'] = d['text'][i]
            print("Gender: " + d['text'][i] +"\n")
        if len(d['text'][i]) == 4 and d['text'][i].isdigit():
            matched_text['Aadhar_No'] = matched_text['Aadhar_No'] +  d['text'][i] + ' '
    return matched_text

def convert_toText(path):

    image = cv2.imread(path)

    # convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # set threshold to identify background and text
    thresholded_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    #perform blurring for noise reduction
    gray = cv2.medianBlur(thresholded_image, 3)

    # Image to text
    text = pytesseract.image_to_string(gray)
    print(text)

    return text
