import cv2
import numpy as np

interval = 30
outfilename = 'output.avi'
threshold=100.
fps = 10
global ret, frame

def detect():
	face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
	img = frame.copy()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = tuple(face_cascade.detectMultiScale(gray, 1.3, 5))

	while faces is ():
		cv2.destroyAllWindows()
		capture()
		togray()
		faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	#print("faces\n\n", faces, "\n\n")

	for (x,y,w,h) in faces:
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	rect1 = (x, y, w, h)
	return img


cap = cv2.VideoCapture(0)
while(1):
	ret, frame = cap.read()
	cv2.imshow("frame",frame)
#	frame = cv2.flip( frame, 1 )
	frame = detect()
	k = cv2.waitKey(1)
	if k == 27:
		break
cv2.destroyAllWindows()
"""
height, width, nchannels = frame.shape

fourcc = cv2.cv2.CV_FOURCC(*'DIVX')
out = cv2.VideoWriter( outfilename,fourcc, fps, (width,height))

ret, frame = cap.read()
frame = imutils.resize(frame, width=500)
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

while(True):

  frame0 = frame

  ret, frame = cap.read()
  frame = imutils.resize(frame, width=500)
  frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

  if not ret:
    deletedcount +=1
    break

  if np.sum( np.absolute(frame-frame0) )/np.size(frame) > threshold:
    out.write(frame)
  else:
    print "Deleted"

  cv2.imshow('Feed - Press "q" to exit',frame)

  key = cv2.waitKey(interval) & 0xFF

  if key == ord('q'):
    print('received key q' )
    break

cap.release()
out.release()
print('Successfully completed')
"""
