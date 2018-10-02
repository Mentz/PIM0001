#! -- coding:utf-8 --

# Colorizador de imagens cinza 
# by: Lucas Litter Mentz

import numpy as np
import cv2
from sys import exit,argv
from math import *

def remap(c, omin, omax, nmin, nmax):
	nc = (c - omin) * (nmax - nmin) / (omax - omin) + nmin
	return nc

def logremap(c, omin, omax, nmin, nmax, a):
	#a = log10(nmax / omax)
	nc = a * log10(c - omin + 1)
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

	# Mapeamento especifico para gonzalez3_10.png
	#r = remap(c, 102, 156, 0, 255); g = b = r
	# Mapeamento logarítmico para figuraEscura.jpg
	r = logremap(c, 0, 19, 0, 255, 195); g = b = r
	# Mapeamento logarítmico para figuraClara.jpg
	#r = logremap(c, 236, 255, 0, 255, 10); g = b = r
	
	global maxr
	maxr = max(maxr, r)

	return (b,g,r)


if __name__ == '__main__':
	x, y, l = 10, 10, 0
	maxr = 0
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
			nimg[i,j] = alargarContraste(img[i,j])
	
	print(maxr)

	newPath = path.split('.')[0]
	cv2.imwrite(newPath + '1.png', nimg)
