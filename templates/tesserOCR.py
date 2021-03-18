import os
import pytesseract
import cv2

#pytesseract.pytesseract.tesseract_cmd = r"C:\Users\AvelinaK\Documents\Machine Learning\tesseract.exe"

TesserOCR_exe_file = 'tesseract.exe'
site_packages_path = 'venv\Lib\site-packages'
CURR_DIRECTORY = os.getcwd()
path_for_sitePackages = os.path.join(os.getcwd(),site_packages_path)
pytesseract.pytesseract.tesseract_cmd = os.path.join(path_for_sitePackages,TesserOCR_exe_file)

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
    #os.remove(path)
    print(text)

    return text