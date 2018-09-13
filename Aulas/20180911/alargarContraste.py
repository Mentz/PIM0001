# Colorizador de imagens cinza 
# by: Lucas Litter Mentz

import numpy as np
import cv2
from sys import exit,argv

def remap(c, omin, omax, nmin, nmax):
	nc = (c - omin) * (nmax - nmin) / (omax - omin) + nmin
	return nc

def clamp(v, vmin, vmax):
	if v < vmin:
		return vmin
	if v > vmax:
		return vmax
	return v

def diff(a, b):
	if a >= b:
		return a - b
	if a < b:
		return b - a

def alargarContraste(c):
	r, g, b = 0, 0, 0
	#margem = 12

	# Mapeamento direto (retorna igual)
	#r,g,b = c,c,c

	if (c < 100):
		r = remap(c, 0, 99, 0, 31); g = b = r;
	elif (100 <= c < 160):
		r = remap(c, 100, 159, 32, 223); g = b = r;
	elif (160 <= c):
		r = remap(c, 160, 255, 224, 255); g = b = r;

	return (b,g,r)


if __name__ == '__main__':
	x, y, l = 10, 10, 0
	path = 'garbage'
	
	''' Ler variaveis da linha de comando '''
	if len(argv) >= 2:
		path = argv[1]
	else:
		print("Uso: python %s <caminho da imagem>\n"
			  "---- O programa gera um arquivo de saida "
			  "(cores_<caminho da imagem>.png) no diretorio atual."
			  % argv[0])
		exit(1)	

	img = cv2.imread(path, 0)
	y, x = len(img), len(img[0])
	nimg = np.zeros((y,x,3), np.uint8)
	for i in xrange(1, y-1):
		for j in xrange(1, x-1):
			nimg[i,j] = colorir(img[i,j])

	newPath = path.split('.')[0]
	cv2.imwrite(newPath + '1.png', nimg)
