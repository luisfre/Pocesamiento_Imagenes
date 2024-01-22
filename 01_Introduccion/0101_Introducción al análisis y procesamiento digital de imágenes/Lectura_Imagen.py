#Descripcion del problema: Se desea leer una imagen de un directorio y guardarla en otro directorio
#Objetivo: obtener la imagen de una carpeta y guardarla en una variable

import numpy as np
import cv2
#Leer una imagen del directorio Imagen
img = cv2.imread('./Imagen/messi.jpg', 0) #ENTRADA: Imagen .jpg

cv2.imwrite('./Guardado/messi_guardado.png', img); #SALIDA: Imagen .jpg

#Mostrar la imagen
cv2.imshow('Imagen', img)
cv2.waitKey(0)
