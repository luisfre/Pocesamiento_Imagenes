#Descripcion del problema: Se desea obtener el histograma RGB de una imagen
#Objetivo: Obtener una imagen RGB del directorio, calcular y graficar su histograma en sus 3 canales R, G y B
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagenes/lena.jpg') #ENTRADA: Imagen RGB .jpg
cv2.imshow('lena.jpg', img)

color = ('b','g','r')

for i, c in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

plt.show() #SALIDA: imagen de origen con su histograma RGB

cv2.destroyAllWindows()