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

def logremap(c, omin, omax, nmin, nmax):
	a = float(nmax) / log10(omax - omin + 1)
	nc = a * log10(c - omin + (1 + nmin))
	return nc

def pow2remap(c, omin, omax, nmin, nmax):
	a = float(nmax) / ((omax - omin) ** 2)
	nc = a * ((c - omin) ** 2)
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

	# Mapeamento direto (retorna igual)
	#r,g,b = c,c,c

	# Mapeamento logarítmico para figuraEscura.jpg
	r = logremap(c, 0, 19, 0, 255); g = b = r
	# Mapeamento logarítmico para figuraClara.jpg
	#r = logremap(c, 236, 255, 0, 255); g = b = r
	
	# Mapeamento quadrado para figuraEscura.jpg
	#r = pow2remap(c, 0, 19, 0, 255); g = b = r
	# Mapeamento quadrado para figuraClara.jpg
	#r = pow2remap(c, 236, 255, 0, 255); g = b = r
	
	global maxr, minr
	maxr = max(maxr, r)
	minr = min(minr, r)

	return (b,g,r)


if __name__ == '__main__':
	x, y, l = 10, 10, 0
	maxr, minr = 0, 0
	path = 'garbage'
	outpath = 'newGarbage'
	
	''' Ler variaveis da linha de comando '''
	if len(argv) >= 3:
		path = argv[1]
		outpath = argv[2]
	else:
		print("Uso: python %s entrada saida\n"
			  "---- O programa gera um arquivo no caminho e extensão "
			  "informados."
			  % argv[0])
		exit(1)	

	img = cv2.imread(path, 0)
	y, x = len(img), len(img[0])
	nimg = np.zeros((y,x,3), np.uint8)
		
	for i in xrange(0, y):
		for j in xrange(0, x):
			nimg[i,j] = alargarContraste(img[i,j])
	
	print(minr)
	print(maxr)

	cv2.imwrite(outpath, nimg)
