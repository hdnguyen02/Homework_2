import cv2

J1 = cv2.imread('lena512color.jpg')

cv2.imshow("Image J1", J1)

J2 = J1.copy()

J2[:, :, 2] = J1[:, :, 0]
J2[:, :, 0] = J1[:, :, 1]
J2[:, :, 1] = J1[:, :, 2]
cv2.imshow("Image J2", J2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('J2.jpg', J2)
