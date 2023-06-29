import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('plant-sp-noise.tif')
assert img is not None, "file could not be read, check with os.path.exists()"
median = cv.medianBlur(img,5)
#blur = cv.blur(img,(5,5))
#Gaussianblur = cv.GaussianBlur(img,(5,5),0)
#bilateral = cv.bilateralFilter(img,9,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
#Cambie aqui los diferentes filtrados
plt.subplot(122),plt.imshow(median),plt.title('Bilateral filtering')
plt.xticks([]), plt.yticks([])
plt.show()