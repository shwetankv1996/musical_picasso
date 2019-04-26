import cv2
import numpy as np
image = cv2.imread('../extracted_images/extracted.jpg') 
# store the height and width of image
height,width = image.shape[:2]
print(image.shape[:2])
quater_height, quater_width = -100, -100
T = np.float32([[1,0,quater_width],[0,1,quater_height]])
img_translation=cv2.warpAffine(image,T,(width,height))
print(T)
cv2.imshow('original_image', image)
cv2.waitKey(0)
cv2.imshow('Translation',img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
