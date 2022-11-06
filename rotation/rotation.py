import cv2
import numpy as np

img = cv2.imread('3.jpg', 0)
height, width = img.shape

arr = np.arange(0, height*width, 1, np.uint8)
rot_img = np.reshape(arr, (height, width))

for i in range(height):
    for j in range(width):
        rot_img[height-i-1][width-j-1] = img[i][j]


cv2.imwrite('rotated.png', rot_img)