import cv2

help(cv2.imread)
help(cv2.imwrite)

J1 = cv2.imread('lenagray.jpg', 0)
J2 = 255 - J1

cv2.imshow("Image J2", J2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('J2.jpeg', J2)
