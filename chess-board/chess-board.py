import cv2
import numpy as np

img = np.arange(0, 640000, 1, np.uint8)
img = np.reshape(img, (800, 800))
height, width = img.shape

for i in range(height):
    for j in range(width):   
        if ((i//(width/8))%2+(j//(width/8))%2)%2==0:
            img[i][j]=255
        else:
            img[i][j]=0

cv2.imwrite('chess-board.png', img)