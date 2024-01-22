#Descripcion del problema: Se desea obtener el negativo de una imagen RGB
#Objetivo: Cambiar todos los canales de color R, G y B de la imagen a su negativo

from PIL import Image

#ENTRADA: una imagen RGB de formato .jpg
foto = Image.open('./imagen/florescolor.jpg')#Obtener la imagen a cambiar

datos = list(foto.getdata()) #Obtengo los datos de color de la imagen

#Cada dato R, G y B le resto de 255 para obtener su valor negativo
datos_invertidos = [(255 - datos[x][0], 255 - datos[x][1], 255 - datos[x][2]) for x in range(len(datos))]

imagen_invertida = Image.new('RGB', foto.size) #Crep una nueva imagen con el tamano de la imagen de entrada

imagen_invertida.putdata(datos_invertidos) #Le anado a la imagen nueva los datos invertidos

#SALIDA: una imagen RGB de formato .jpg con los canales invertidos de la imagen original
imagen_invertida.save('./negativo/floresnegativo.jpg') #Guardo la imagen resultante en un directorio especifico

#Cierro las imagenes
imagen_invertida.close()

foto.close()