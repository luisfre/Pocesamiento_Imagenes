#PROBLEMA:Utilizacion de filtros con mascaras de convolucion
#DESCRIPCION:Este programa utiliza un metodo matematico de convolucion para aplicarle un filtro laplaciano a una imagen
#OBJETIVO:Conocer y entender un poco mejor las mascaras de convolucion


import numpy as np
import cv2
from tkinter import *
#Creacion de interfaz grafica(gui)
contenedor=Tk()
contenedor.title("Filtro Laplaciano")
mFrame=Frame(contenedor,width=200,height=200)
mFrame.pack()
label1=Label(mFrame,text="ingrese la ruta del archivo: ")
label1.grid(row=0,column=0,padx=5,pady=40)
fichero=StringVar()
cText=Entry(mFrame,textvariable=fichero)
cText.grid(row=0,column=1,padx=5,pady=40)

#Metodo matematico de convolucion
def convolucion(imagen,filtro):
    aux=np.zeros((imagen.shape[0],imagen.shape[1]),dtype=np.int)
    for i in (range(1,imagen.shape[0]-1)):
        for j in (range(1,imagen.shape[1]-1)):
            pix=imagen.item(i-1,j-1)*filtro[0][0]+imagen.item(i-1,j)*filtro[0][1]+imagen.item(i-1,j+1)*filtro[0][2]+imagen.item(i,j-1)*filtro[1][0]+imagen.item(i,j)*filtro[1][1]+imagen.item(i,j+1)*filtro[1][2]+imagen.item(i+1,j-1)*filtro[2][0]+imagen.item(i+1,j)*filtro[2][1]+imagen.item(i+1,j+1)*filtro[2][2]
            if pix>255:
                pix=255
            elif pix<0:
                    pix=0
            aux.itemset((i,j),pix)

    aux=aux.astype(np.uint8)
    return aux



def codigoBoton():
    #Cargar imagenes guardadas
    imgOrig=cv2.imread(fichero.get())
    #convertir la imagen cargada a escala de grises
    imgGris=cv2.cvtColor(imgOrig,cv2.COLOR_RGB2GRAY)
    #matriz de laplace
    filtroLaplaciano=([[0,1,0],[1,-4,1],[0,1,0]])
    #llamar al metodo convolucion()
    imgConver=convolucion(imgGris,filtroLaplaciano)
    #Mostrar imagenes en diferentes ventanas
    cv2.imshow('IMAGEN ORIGINAL',imgOrig)
    cv2.imshow('IMAGEN ESCALA DE GRISES',imgGris)
    cv2.imshow('IMAGEN FILTRADA',imgConver)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



#Accion del boton invocando al metodo codigoBoton()
boton=Button(mFrame,text="Procesar imagen",command=codigoBoton)
boton.grid(row=1,column=1,padx=5,pady=3)

contenedor.mainloop()



       

                   









