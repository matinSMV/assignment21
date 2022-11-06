import cv2

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

inverted_img1 = cv2.bitwise_not(img1)
inverted_img2 = cv2.bitwise_not(img2)

cv2.imwrite('correct-1.png', inverted_img1)
cv2.imwrite('correct2.png', inverted_img2)