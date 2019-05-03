import numpy as np
import cv2 as cv
import sys

global rect
rect = (0,0,1,1)


def togray():
	global img, img2
	img = cv.imread(filename)
	img2 = img.copy()
	global gray
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


if len(sys.argv) == 2:
	filename = sys.argv[1] # for drawing purposes
else:
	print("No input image given, so loading default image, lena.jpg \n")
	print("Correct Usage: python grabcut.py <filename> \n")
	filename = 'lena.jpg'

face_cascade = cv.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
togray()
faces = tuple(face_cascade.detectMultiScale(gray, 1.3, 5))

while faces is ():
	cv.destroyAllWindows()
#	capture()
	togray()
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
rect = (x, y, x+w, y+h)
print("\n\n", rect, "\n\n")


cv.imshow('image', img)
cv.waitKey(0)
# [display]
cv.destroyAllWindows()
