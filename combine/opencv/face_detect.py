import numpy as np
import cv2 as cv
import sys


BLUE = [255,0,0]        # rectangle color
RED = [0,0,255]         # PR BG
GREEN = [0,255,0]       # PR FG
BLACK = [0,0,0]         # sure BG
WHITE = [255,255,255]   # sure FG


"""
..............................................................................................................
Capture image starts
..............................................................................................................
"""
def capture():
	cap = cv.VideoCapture(0)
	ret, frame = cap.read()
	cv.imwrite('/home/sv-v1/projects/picasso/images/capture.jpg', frame)

"""
..............................................................................................................
Capture image ends
..............................................................................................................
"""

"""
..............................................................................................................
Convert image to gray starts
..............................................................................................................
"""
def togray():
	global img, img2
	img = cv.imread('/home/sv-v1/projects/picasso/images/capture.jpg')
	img2 = img.copy()
	global gray
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
"""
..............................................................................................................
Convert image to gray ends
..............................................................................................................
"""

"""
..............................................................................................................
Magic wand touchup starts
..............................................................................................................
"""
def magic():
	rect = (0,0,1,1)
	mask = np.zeros(img.shape[:2],dtype = np.uint8) # mask initialized to PR_BG
	bgdmodel = np.zeros((1,65),np.float64)
	fgdmodel = np.zeros((1,65),np.float64)
	cv.grabCut(img2,mask,rect,bgdmodel,fgdmodel,1,cv.GC_INIT_WITH_RECT)
	mask2 = np.where((mask==1) + (mask==3),255,0).astype('uint8')
	output = cv.bitwise_and(img2,img2,mask=mask2)
	return output
"""
.............................................................................................................. 
Magic wand touchup ends
..............................................................................................................
"""

"""
..............................................................................................................
Face Detection starts
..............................................................................................................
"""

face_cascade = cv.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml')
#img = cv.imread('/home/sv-v1/projects/picasso/images/capture.jpg')
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
togray()
capture()
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
cv.waitKey(0)
cv.destroyAllWindows()

while faces is ():
	cv.destroyAllWindows()
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	capture()
	togray()

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
img_new = magic()
cv.imshow('img',img_new)
cv.waitKey(0)
cv.destroyAllWindows()

