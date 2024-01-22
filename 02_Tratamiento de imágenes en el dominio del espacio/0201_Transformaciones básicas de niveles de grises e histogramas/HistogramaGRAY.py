#Descripcion del problema: Se desea obtener el histograma de una imagen en escala de grises
#Objetivo: Obtener una imagen del directorio en grises, distribuir el color ecualizandola y  por último calcular y graficar su histograma

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagenes/lena.jpg', cv2.IMREAD_GRAYSCALE) #ENTRADA: Imagen .jpg leida en escala de grises
cv2.imshow('lena.jpg', img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256]) #calculamos su histograma de grises
plt.plot(hist, color='gray')
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

img = cv2.equalizeHist(img) #ecualiza la imagen, distribuye el color
cv2.imshow('lenaEcualizada.jpg', img)

hist1 = cv2.calcHist([img], [0], None, [256], [0, 256]) #histograma imagen ecualizada
plt.plot(hist1, color='gray')
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')

plt.show() #SALIDA: Imagen de origen con su histograma, imagen ecualizada con su histograma

cv2.destroyAllWindows()