import cv2
import numpy as np

image = cv2.imread('/content/Laboratory_image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gradients_sobelx = cv2.Sobel(image, -1, 1, 0)
gradients_sobely = cv2.Sobel(image, -1, 0, 1)
gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely,0.5, 0)
gradient_laplacian = cv2.Laplacian(image, -1)
canny_output = cv2.Canny(image, 50, 200)

cv2.imwrite('gradients_sobelx.jpg', gradients_sobelx)
cv2.imwrite('gradients_sobely.jpg', gradients_sobely)
cv2.imwrite('gradients_sobelxy.jpg', gradients_sobelxy)
cv2.imwrite('gradient_laplacian.jpg', gradient_laplacian)
cv2.imwrite('canny_output.jpg', canny_output)
cv2.waitKey()
