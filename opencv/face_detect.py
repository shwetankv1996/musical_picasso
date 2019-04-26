import numpy as np
import cv2 as cv
import sys


BLUE = [255,0,0]        # rectangle color
RED = [0,0,255]         # PR BG
GREEN = [0,255,0]       # PR FG
BLACK = [0,0,0]         # sure BG
WHITE = [255,255,255]   # sure FG
image_path = '/home/sv-v1/projects/picasso/images/capture.jpg'
image_magic_path = '/home/sv-v1/projects/picasso/extracted_images/extracted.jpg'
alpha = 0.4
global rect1, rect2
rect1 = (0,0,1,1)
rect2 = (0,0,1,1)


"""
..............................................................................................................
Capture image starts
..............................................................................................................
"""
def capture():
	cap = cv.VideoCapture(0)
	ret, frame = cap.read()
	cv.imwrite(image_path, frame)

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
	img = cv.imread(image_path)
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
	cv.imshow('img2',img2)
	mask = np.zeros(img.shape[:2],dtype = np.uint8) # mask initialized to PR_BG
	output = np.zeros(img.shape,np.uint8)           # output image to be shown
	bgdmodel = np.zeros((1,65),np.float64)
	fgdmodel = np.zeros((1,65),np.float64)
	cv.grabCut(img2,mask,rect1,bgdmodel,fgdmodel,1,cv.GC_INIT_WITH_RECT)
	mask2 = np.where((mask==1) + (mask==3),255,0).astype('uint8')
	output = cv.bitwise_and(img2,img2,mask=mask2)
#	cv.rectangle(output,(x,y),(x+w,y+h),(255,0,0),1)
	cv.imwrite(image_magic_path, output)
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
#def detect():

face_cascade = cv.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
capture()
img = cv.imread(image_path)
togray()
faces = tuple(face_cascade.detectMultiScale(gray, 1.3, 5))

while faces is ():
	cv.destroyAllWindows()
	capture()
	togray()
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
#print("faces\n\n", faces, "\n\n")

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
rect1 = (x, y, w, h)
print("rect1\n\n", rect1, "\n\n")
"""
..............................................................................................................
Face Detection ends
..............................................................................................................
"""

#detect()


img2 = img.copy()
img_new = magic()
cv.imshow('img',img)
cv.imshow('img_new',img_new)

while(1):
	k = cv.waitKey(0)
	if k == 27:
		break
	elif k == ord('m'):
		print("pressed\n")
		img_new = magic()	
	cv.imshow('img',img)
	cv.imshow('img2',img2)
	cv.imshow('img_new',img_new)

cv.destroyAllWindows()


print("blending now\n")
src1 = cv.imread(cv.samples.findFile(image_magic_path))
src2 = cv.imread(cv.samples.findFile('../images/the_joker.jpg'))


src2_gray = cv.cvtColor(src2, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(src2_gray, 1.1, 5)
for (x,y,w,h) in faces:
    cv.rectangle(src2,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
rect2 = (x,y,w,h)
cv.imshow("src2", src2)
cv.waitKey(0)
cv.destroyAllWindows()

src1_gray = cv.cvtColor(src1, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(src1_gray, 1.1, 5)
for (x,y,w,h) in faces:
    cv.rectangle(src1,(x,y),(x+w,y+h),(0,255,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
rect1 = (x,y,w,h)
cv.imshow("src2", src2)
cv.imshow("src1", src1)
cv.waitKey(0)
cv.destroyAllWindows()


mask_src2 = np.zeros(src2.shape[:2],dtype = np.uint8) # mask initialized to PR_BG
cv.rectangle(mask_src2, (rect2[0], rect2[1]), (rect2[0]+rect2[2], rect2[1]+rect2[3]), (255, 255, 255), -1)
mask_src2 = cv.bitwise_not(mask_src2)
src2 = cv.bitwise_and(src2,src2,mask=mask_src2)
cv.imshow("src2", src2)

cv.waitKey(0)
cv.destroyAllWindows()

h1, w1, d1 = src1.shape
h2, w2, d2 = src2.shape
s1 = h2/h1
s2= w2/w1

newx = rect1[0] * s1
newy = rect1[1] * s2
newh = h1*s1
neww = w1*s2
rect1_scaled = rect1
rect1_scaled = (int(newx), int(newy), int(newh), int(neww))
print("rect\n",rect2)
print(rect1_scaled)
print(rect1)

#rect_diff = (rect2[0] - rect1[0]) **2 + (rect2[1] - rect1[1]) **2 + (rect2[2] - rect1[2]) **2 + (rect2[3] - rect1[3]) **2
rect_diff = np.subtract(rect2, rect1)
print("diff\n",rect_diff)

T = np.float32([[1,0,rect_diff[0]],[0,1,rect_diff[1]]])
img_translation=cv.warpAffine(src1,T,(w1, h1))
cv.imshow("src1", img_translation)
cv.waitKey(0)
cv.destroyAllWindows()

src1 = cv.resize(src1, (int(neww), int(newh)))
cv.waitKey(0)
# [display]
cv.destroyAllWindows()
beta = (1.0 - alpha)
dst = cv.addWeighted(src1, alpha, src2, beta, 0.3)
cv.imshow('dst', dst)
cv.waitKey(0)
# [display]
cv.destroyAllWindows()
