# Colorizador de imagens cinza
# by: Lucas Litter Mentz

import numpy as np
import cv2
from sys import exit,argv

fundo = 0

def limiarizar(img, limiar):
	y, x = len(img), len(img[0])
	nimg = np.zeros((y, x), np.uint8)
	for i in xrange(0, y):
		for j in xrange(0, x):
			if img[i,j] >= limiar:
				nimg[i,j] = 1
	return nimg

def rotular(label, img, aux, y, x):
	aux[y, x] = label
	pos = (y,x)
	vis = [(),(),(),()]
	''' Acima, direita, abaixo, esquerda '''
	if y > 0:
		if img[y,x] == img[y-1, x]: rotular(label, img, aux, y-1, x)
	if x < len(img[0]) - 1:
		if img[y,x] == img[y, x+1]: rotular(label, img, aux, y, x+1)
	if y < len(img) - 1:
		if img[y,x] == img[y+1, x]: rotular(label, img, aux, y+1, x)
	if x > 0:
		if img[y,x] == img[y, x-1]: rotular(label, img, aux, y, x-1)

def identify(img):
	y, x = len(img), len(img[0])
	aux = np.zeros((y, x), np.uint32)
	for i in xrange(0, y):
		for j in xrange(0, x):
			if img[i,j] != fundo and aux[i,j] == -1:
				rotular(label, img, aux, i, j)


if __name__ == '__main__':
	x, y, l = 10, 10, 0
	path = 'garbage'

	''' Ler variaveis da linha de comando '''
	if len(argv) >= 3:
		path = argv[1]
		fundo = int(argv[2])
	else:
		print("Uso: python %s <caminho da imagem> <fundo>\n"
			  "     fundo: 0 para preto, 1 para branco\n"
			  "---- O programa gera um arquivo de saida "
			  "(<caminho da imagem>_segmentada.png) no diretorio atual."
			  % argv[0])
		exit(1)

	img = cv2.imread(path, 0)
	y, x = len(img), len(img[0])
	nimg = limiarizar(img, 126)
	aux = identify(nimg)

	newPath = path.split('.')[0]
	cv2.imwrite(newPath + 'segmentada.png', nimg)
