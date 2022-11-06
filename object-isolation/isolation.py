import cv2

img = cv2.imread('4.jpg', 0)
height, width = img.shape

for i in range(height):
    for j in range(width):
        if img[i][j]<120:
            img[i][j] = 0

cv2.imwrite('isolated.png', img)