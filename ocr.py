import cv2
import pytesseract
import numpy as np


# tell pytesseract where tesseract engine is located
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\AvelinaK\Documents\Machine Learning\tesseract.exe"

img = cv2.imread("computer-vision.jpg")

#img = perspective_transform()

# Image preprossessing techniques

# image resizing
img =cv2.resize(img,None,fx=0.5, fy=0.5 , interpolation= cv2.INTER_AREA)

# convert image to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# set threshold to identify background and text
#Custom value gets removed from the threshold  - if this parameter decreases more noise, increases- text clarity reduced and less noise
# blocksize - increses -> more noise but text will be clear  , decreases -> text unclear
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 11)

# noise removal
denoise = cv2.fastNlMeansDenoising(adaptive_threshold,None,10,7,21)

# morphological image transformations

#erosion
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(denoise,kernel,iterations = 1)

dilation = cv2.dilate(erosion,kernel,iterations = 1)


#ocr configs: page segmentation mode
# 3 is the default
#config = "--psm 3"

# Image to text
text = pytesseract.image_to_string(adaptive_threshold)
print(text)

cv2.imshow("adaptive", adaptive_threshold)
# to keep the image open
cv2.waitKey(0)
