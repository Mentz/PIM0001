#! coding: UTF-8 !
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

def equalizarContraste(img):
	x, y = len(img), len(img[0])
	new_img = np.zeros((x, y, 3), np.uint8)
	# MN é a área da imagem ou quantidade de pixels (x*y)
	MN = float(x*y)
	# L é a profundidade de cor (cinza)
	L = 256

	# TODO: fazer as coisas aqui
	# gerar contagem do histograma
	hist = [0]*L
	for i in img:
		for c in i:
			hist[c] += 1

	# gerar o valor de saida (sk)
	s = [0]*L
	g1 = (L - 1)/MN
	for k in xrange(0, 256):
		g2 = 0
		for j in range(0, k+1):
			g2 += hist[j]
		s[k] = int(round(g1 * g2))

	# reaplicar os valores para cada pixel usando s[k]
	for j in xrange(y):
		for i in xrange(x):
			new_img[i, j] = [s[img[i, j]]]*3

	return new_img


if __name__ == '__main__':
	x, y, l = 10, 10, 0
	path = 'garbage'

	''' Ler variaveis da linha de comando '''
	if len(argv) >= 2:
		path = argv[1]
	else:
		print("Uso: python %s <caminho da imagem>\n"
			  "---- O programa gera um arquivo de saida "
			  "(<caminho da imagem>_eq.png) no diretorio atual."
			  % argv[0])
		exit(1)

	img = cv2.imread(path, 0)
	nimg = equalizarContraste(img)

	newPath = path.split('.')[0]
	cv2.imwrite(newPath + '_eq.png', nimg)
