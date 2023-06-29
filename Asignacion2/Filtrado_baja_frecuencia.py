import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#!!!!! ASEGURAR QUE IMAGENES ESTEN EN LA MISMA CARPETA QUE EL PROGRAMA !!!!!!#

#Simplemente eliminar comentarios para probar las imagenes

img = cv.imread('plant-sp-noise.tif', cv.IMREAD_GRAYSCALE)
#img = cv.imread('ophrys.tif', cv.IMREAD_GRAYSCALE)


assert img is not None, "file could not be read, check with os.path.exists()"

#Elegir que filtro utilizar y cambiar mas abajo
median = cv.medianBlur(img,5)
#blur = cv.blur(img,(5,5))
#Gaussianblur = cv.GaussianBlur(img,(5,5),0)
#bilateral = cv.bilateralFilter(img,9,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
#Cambiar aqui los diferentes filtrados
plt.subplot(122),plt.imshow(median),plt.title('Filtro Aplicado')
plt.xticks([]), plt.yticks([])
plt.show()