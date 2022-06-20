import cv2

print("Printing Back to the Future...")

filePath = 'B2TF.jpg'
img = cv2.imread(filePath, 1)
cv2.imshow("B2TF", img)
cv2.waitKey(0)
cv2.destroyAllWindows()