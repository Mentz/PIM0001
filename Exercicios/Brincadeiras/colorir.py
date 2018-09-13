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
	r,g,b,bb = [0]*4
	margem = 12

	if diff(c, 106) < margem:
		r+=206;g+=79;b+=81
		bb += 1
	if diff(c, 128) < margem:
		r+=80;g+=136;b+=186
		bb += 1
	if diff(c, 160) < margem:
		r+=239;g+=147;b+=61
		bb += 1
	
	if bb > 0:
		r/=bb;g/=bb;b/=bb
		return (b,g,r)
	return (c,c,c)

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
	for i in xrange(0, y):
		for j in xrange(0, x):
			nimg[i,j] = colorir(img[i,j])

	newPath = path.split('.')[0]
	cv2.imwrite(newPath + '_colorido.png', nimg)
