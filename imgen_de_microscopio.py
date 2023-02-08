
import cv2

img = cv2.imread('imagen_de_microscopio.jpg')
    
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
   
AND = cv2.bitwise_and(img,bw_img)  

cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('AND',AND)
cv2.waitKey(0)
cv2.destroyAllWindows()