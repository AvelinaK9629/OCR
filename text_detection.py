import craft
import cv2

img = cv2.imread('Testproc1.jpg')

# run the detector
bboxes, polys, heatmap = craft.detect_text(img)

# view the image with bounding boxes
img_boxed = craft.show_bounding_boxes(img, bboxes)
cv2.imshow('fig', img_boxed)
cv2.waitKey(0)

# view detection heatmap
cv2.imshow('fig', heatmap)
cv2.waitKey(0)