import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\AvelinaK\Documents\Machine Learning\tesseract.exe"

#img = cv2.imread("noisy_img.png")
#img = cv2.imread("example_02.png")
img = cv2.imread("Testproc1.jpg")

resize = cv2.resize(img,None,fx=1, fy=1, interpolation= cv2.INTER_AREA)

gray = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)

thresh, bw_img = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(bw_img,kernel,iterations = 1)

#opening = cv2.morphologyEx(bw_img, cv2.MORPH_OPEN, kernel)

#closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

#filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
#sharpen_img = cv2.filter2D(closing,-1,filter)

text = pytesseract.image_to_string(erosion)
print(text)

cv2.imshow("IMAGE", erosion)
# to keep the image open
cv2.waitKey(0)