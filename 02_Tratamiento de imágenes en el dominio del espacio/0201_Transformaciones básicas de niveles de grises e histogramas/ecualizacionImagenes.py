#Descripcion del proyecto: Distribuir el color de una imagen equitativamente
#Objetivo: Ecualizar la imagen a tratar para distribuir su color

import cv2

#ENTRADA: Imagen .jpg
img = cv2.imread('imagenes/lena.jpg', cv2.IMREAD_GRAYSCALE) #lee la imagen en escala de grises
cv2.imshow(' ', img)

img = cv2.equalizeHist(img) #ecualiza la imagen, distribuye el color

cv2.imshow('Imagen ecualizada', img) #SALIDA: Imagen ecualizada en una ventana
cv2.waitKey()