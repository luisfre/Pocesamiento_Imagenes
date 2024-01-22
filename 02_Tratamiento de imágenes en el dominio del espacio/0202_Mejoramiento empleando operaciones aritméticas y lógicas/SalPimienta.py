#Descripcion del problema: se requiere limpiar o reducir el ruido en una imagen con ruido impulsional o sal y pimienta
#Objetivo: reducir el rudio de sal y pimienta de una imagen aplicando el filtro de la media por medio de convolucion

from PIL import Image, ImageFilter
i=0

#ENTRADA: Imagen con ruido impulsional .jpg
foto = Image.open('./imagenes/salt_and-pepper_noise.jpg')

#a una nueva variable le asigno mi imagen aplicandole el filtro de la media
nuevaImagen = foto.filter(ImageFilter.MedianFilter(size=3))

while i <  6:
    #Aplico el filtro de la media a la nueva imagen y la guardo
    nuevaImagen = nuevaImagen.filter(ImageFilter.MedianFilter(size=3))
    
    #SALIDA: Imagen .jpg con menor reuido despues de aplicar el filtro de la media
    nuevaImagen.save('./imagenes/imagenLimpia' + str(i) + '.jpg')
    Image.open('./imagenes/imagenLimpia' + str(i) + '.jpg').show()
    i += 1

foto.close()

nuevaImagen.close()