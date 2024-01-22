# Ejemplo tomado de:
# April 22, 2019
# Tran Le Anh - MSc Student in Computer Vision
# Dept. of Electronics Engineering, Myongji University, South Korea
# tranleanh.nt@gmail.com
# https://sites.google.com/view/leanhtran

#Descripción del problema: Se desea aplicar un filtro basado en la transformada de Fourier
#Objetivo: Aplicar la transformada de Fourier mediante el filtro de Wienerm, con ayuda de opencv

import os
import numpy as np
from numpy.fft import fft2, ifft2
from scipy.signal import gaussian, convolve2d
import matplotlib.pyplot as plt

# Función desenfocar: para que la imagen original pierda nitidez
def blur(img, kernel_size = 3):
	dummy = np.copy(img) #Permite tener un mayor control sobre la memoria, produce un array
	h = np.eye(kernel_size) / kernel_size #Retorna una matriz cuya diagonal está llena de unos y el resto lleno de ceros
	dummy = convolve2d(dummy, h, mode = 'valid')
	return dummy
# Función de ruido gaussiano: para producir pequeñas variaciones en la imagen
def add_gaussian_noise(img, sigma):
	gauss = np.random.normal(0, sigma, np.shape(img))
	noisy_img = img + gauss
	noisy_img[noisy_img < 0] = 0
	noisy_img[noisy_img > 255] = 255
	return noisy_img

# Función de filtro Wiener
def wiener_filter(img, kernel, K):
	kernel /= np.sum(kernel) #Esta función retorna la suma de los elementos de un arreglo
	dummy = np.copy(img)
	dummy = fft2(dummy)
	kernel = fft2(kernel, s = img.shape)
	kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)#El método abs calcula el valor absoluto
	dummy = dummy * kernel
	dummy = np.abs(ifft2(dummy)) 
	return dummy

# Función crear kernel gaussiano
#El kernel gaussiano es un producto escalar en un espacio transformado de dimensión infinita
def gaussian_kernel(kernel_size = 3):
	h = gaussian(kernel_size, kernel_size / 3).reshape(kernel_size, 1)
	h = np.dot(h, h.transpose())
	h /= np.sum(h)
	return h

# Función para convertir en escala de grises
def rgb2gray(rgb):
	return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

# Función principal y llamada de todas las funciones antes definidas
if __name__ == '__main__':
	# cargar imagen y convertir en escala de grises
	file_name = os.path.join('./imagenes/lena1960.jpg')
	img = rgb2gray(plt.imread(file_name))

	# Desenfocar la imagen
	blurred_img = blur(img, kernel_size = 15)

	# Añadir ruido gaussiano
	noisy_img = add_gaussian_noise(blurred_img, sigma = 20)

	# Aplicar Wiener Filter
	kernel = gaussian_kernel(3)
	filtered_img = wiener_filter(noisy_img, kernel, K = 10)

	# Visualizar resultados
	display = [img, blurred_img, noisy_img, filtered_img]
	label = ['Image Original', 'Movimiento Imagen borrosa', 'Desenfoque por movimiento + Ruido Gaussiano', 'Filtro Wiener aplicado']

	fig = plt.figure(figsize=(12, 10))

	for i in range(len(display)):
		fig.add_subplot(2, 2, i+1)
		plt.imshow(display[i], cmap = 'gray')
		plt.title(label[i])

	plt.show()