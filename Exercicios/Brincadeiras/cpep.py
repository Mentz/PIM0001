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

def colorir(c):
	r, g, b = 0, 0, 0

	if diff(c, 10) < 2:
		r,g,b = 206,79,81
	elif diff(c, 251) < 2:
		r,g,b = 80,136,186
	else:
		r = c
		g = r
		b = r
	
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
			media = (img[i][j])
			nimg[i,j] = colorir(media)

	newPath = path.split('.')[0]
	cv2.imwrite('cores_' + newPath + '.png', nimg)
