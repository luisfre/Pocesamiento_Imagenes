#PROBLEMA:Cambio entre los espacios de color
#DESCRIPCION:Este programa realiza todas conversiones entre los distintos espacios de color que maneja la funcion opencv
#OBJETIVO:Conocer las facilidades que preporciona opencv para poder convertir el espacio RGB en distintos espacios de color

import cv2 as cv

#Funcion de opencv para la carga de imagenenes
img=cv.imread('imagenes/prueba.jpg')
#Funcion de opencv para la mostrar  imagenes en pantalla
cv.imshow('IMAGEN Original', img)
cv.waitKey(0)
cv.destroyAllWindows()


#xyz
#Funcion de opencv para convertir imagenes de rgb a xyz
imgxyz=cv.cvtColor(img, cv.COLOR_RGB2XYZ)
#Division de canales
ch1 = imgxyz[:, :, 0]
ch2 = imgxyz[:, :, 1]
ch3 = imgxyz[:, :, 2]
#Mostrar la imagen transformada y los distintos canales
cv.imshow('IMAGEN CIE XYZ',imgxyz)
cv.imshow('COMPONENTE 1',ch1)
cv.imshow('COMPONENTE 2',ch2)
cv.imshow('COMPONENTE 3',ch3)
cv.waitKey(0)
cv.destroyAllWindows()
#Hue- Matiz, Saturation- Saturación, Lightness- Luminosidad
#HSL
#Funcion de opencv para convertir imagenes de rgb a hsl
imghsl=cv.cvtColor(img, cv.COLOR_RGB2HLS_FULL)
#Division de canales
ch1 = imghsl[:, :, 0]
ch2 = imghsl[:, :, 1]
ch3 = imghsl[:, :, 2]
#Mostrar la imagen transformada y los distintos canales
cv.imshow('IMAGEN HSL',imghsl)
cv.imshow('COMPONENTE 1',ch1)
cv.imshow('COMPONENTE 2',ch2)
cv.imshow('COMPONENTE 3',ch3)
cv.waitKey(0)
cv.destroyAllWindows()

#Matiz, Saturación, Valor
#HSV
#Funcion de opencv para convertir imagenes de rgb a hsv
imghsv=cv.cvtColor(img, cv.COLOR_RGB2HSV)
#Division de canales
ch1 = imghsv[:, :, 0]
ch2 = imghsv[:, :, 1]
ch3 = imghsv[:, :, 2]
#Mostrar la imagen transformada y los distintos canales
cv.imshow('IMAGEN LAB',imghsv)
cv.imshow('COMPONENTE 1',ch1)
cv.imshow('COMPONENTE 2',ch2)
cv.imshow('COMPONENTE 3',ch3)
cv.waitKey(0)
cv.destroyAllWindows()

# L* es luminosidad de negro a blanco, A o a* va de rojo a verde y B o b* es la gradiente del azul.
#LAB
#Funcion de opencv para convertir imagenes de rgb a lab
imglab=cv.cvtColor(img, cv.COLOR_RGB2LAB)
#Division de canales
ch1 = imglab[:, :, 0]
ch2 = imglab[:, :, 1]
ch3 = imglab[:, :, 2]
#Mostrar la imagen transformada y los distintos canales
cv.imshow('IMAGEN LAB',imglab)
cv.imshow('COMPONENTE 1',ch1)
cv.imshow('COMPONENTE 2',ch2)
cv.imshow('COMPONENTE 3',ch3)
cv.waitKey(0)
cv.destroyAllWindows()

# Y' representan la componente de luma y las señales CB y CR son los componentes de crominancia diferencia de azul y diferencia de rojo, respectivamente. Y' se
# diferencia de Y en que es la señal de luma codificada de manera no lineal basada en las señales primarias RGB con corrección gamma.
##YCrCb
#Funcion de opencv para convertir imagenes de rgb a YCrCb
imgycrcb=cv.cvtColor(img, cv.COLOR_RGB2YCrCb)
#Division de canales
ch1c = imgycrcb[:, :, 0]
ch2c = imgycrcb[:, :, 1]
ch3c = imgycrcb[:, :, 2]
#Mostrar la imagen transformada y los distintos canales
cv.imshow('IMAGEN YCrCb',imgycrcb)
cv.imshow('COMPONENTE 1',ch1c)
cv.imshow('COMPONENTE 2',ch2c)
cv.imshow('COMPONENTE 3',ch3c)
cv.waitKey(0)
cv.destroyAllWindows()