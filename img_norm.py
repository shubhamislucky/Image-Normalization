import cv2 as cv
import numpy as np

img = cv.imread('city.jpeg')
norm_img = np.zeros((800,800))
final_img = cv.normalize(img,  norm_img, 0, 255, cv.NORM_MINMAX)
cv.imshow('Normalized Image', final_img)
cv.imwrite('city_normalized.jpg', final_img)
cv.waitKey(0)
cv.destroyAllWindows()