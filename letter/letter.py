import cv2
import numpy as np

img_arr = np.arange(0, 90000, 1, np.uint8)
img = np.reshape(img_arr, (300, 300))
height, width = img.shape

img[:,:]=255
img[100:250, 30:60]=0
img[100:250, 160:190]=0

img[100:130, 60:90]=0
img[120:150, 70:100]=0
img[140:180, 80:110]=0

img[160:200, 90:130]=0

img[140:180, 110:140]=0
img[120:150, 120:150]=0
img[100:130, 130:160]=0



cv2.imwrite('letter.png', img)
