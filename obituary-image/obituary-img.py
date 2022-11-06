import cv2

img = cv2.imread('paul-walker.png', 0)

height, width = img.shape

for i in range(300): 
    for j in range(40): 
        if not 100-i+j<0:
            img[i][100-i+j]= 0

cv2.imwrite('deceased.png', img)