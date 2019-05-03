import cv2
import numpy as np 

# Read images
src = cv2.imread("images/airplane.jpg")
dst = cv2.imread("images/sky.jpg")

#print(src.shape[:2])
# Create a rough mask around the airplane.

src_mask = np.zeros(src.shape, src.dtype)
poly = np.array([ [4,80], [30,54], [151,63], [254,37], [298,90], [272,134], [43,122] ], np.int32)
cv2.fillPoly(src_mask, [poly], (255, 255, 255))
cv2.imshow("mask", src_mask)
#cv2.imshow("dst", dst)
#cv2.imshow("src", src)
# This is where the CENTER of the airplane will be placed
center = (0,0)
#print(roi.x)
#print(roi.y)
#print(roi.width)
#print(roi.height)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Clone seamlessly.
output = cv2.seamlessClone(src, dst, src_mask, center, cv2.NORMAL_CLONE)

# Write result
cv2.imwrite("images/cloning-example.jpg", output);

