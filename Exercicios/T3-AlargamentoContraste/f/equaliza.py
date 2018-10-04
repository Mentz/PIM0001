#! coding: UTF-8 !
# Colorizador de imagens cinza
# by: Lucas Litter Mentz

import numpy as np
import cv2
from sys import exit,argv

def BGR_to_YUV(img):
	new_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
	return new_img

def YUV_to_BGR(img):
	new_img = cv2.cvtColor(img, cv2.COLOR_YUV2BGR)
	return new_img

def equalizarContraste(img):
	y, x = len(img), len(img[0])
	new_img = img.copy()
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
	for k in range(0, 256):
		g2 = 0
		for j in range(0, k+1):
			g2 += hist[j]
		s[k] = int(round(g1 * g2))

	print(s)

	# reaplicar os valores para cada pixel usando s[k]
	for i in range(y):
		for j in range(x):
			# nova_img    = (equalizacao de y)
			new_img[i, j] = s[img[i, j]]

	return new_img


if __name__ == '__main__':
	x, y, l = 10, 10, 0
	path = 'garbage'
	outpath = 'newGarbage'


	''' Ler variaveis da linha de comando '''
	if len(argv) >= 3:
		path = argv[1]
		outpath = argv[2]
	else:
		print("Uso: python %s <caminho da imagem>\n"
			  "---- O programa gera um arquivo de saida "
			  "(<caminho da imagem>_eq.png) no diretorio atual."
			  % argv[0])
		exit(1)

	img = cv2.imread(path)
	img_yuv = BGR_to_YUV(img)
	img_y, img_u, img_v = cv2.split(img_yuv)
	nimg_y = equalizarContraste(img_y)
	nimg_yuv = cv2.merge((nimg_y, img_u, img_v))
	nimg = YUV_to_BGR(nimg_yuv)

	cv2.imwrite(outpath, nimg)
