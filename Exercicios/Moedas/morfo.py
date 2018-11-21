#!/usr/bin/env python3
#! - coding: UTF8 -

# Instalar os requisitos:
# python3 -m pip install -U scikit-image scikit-learn matplotlib numpy opencv-python

from matplotlib import pyplot
import skimage.morphology as skm
import skimage.filters as skf
import sys
import numpy as np
import cv2


def limiarizar(img):
	limiar = skf.threshold_otsu(img)
	# y, x = len(img), len(img[0])
	# out = np.zeros((y, x, 3), np.uint8)
	# for i in range(y):
	# 	for j in range(x):
	# 		out[i][j] = (0, 0, 0) if img[i][j] > limiar else (255,255,255)
	# return out
	out = img < limiar
	return out

def toBGR(img):
	y,x = len(img), len(img[0])
	out = np.zeros((y,x,3), np.uint8)
	for i in range(y):
		for j in range(x):
			out[i][j] = (0,0,0) if img[i][j] == 0 else (255,255,255)
	return out

# NÃO PRECISA IMPLEMENTAR DILATAÇÃO E EROSÃO
# O objetivo é usar abertura e fechamento para contagem
# de moedas em uma foto que está no seu celular, Mentz!
# Biblioteca:
# pymorph ou skimage
# Usar limiarização de OTSU

def dilatacao(img, est):
	out = skm.binary_dilation(img, est)
	return out

def erosao(img, est):
	out = skm.binary_erosion(img, est)
	return out
	
def abertura(img, est):
	img2 = erosao(img, est)
	out = dilatacao(img2, est)
	return out
	
def fechamento(img, est):
	img2 = dilatacao(img, est)
	out = erosao(img2, est)
	return out

if __name__ == "__main__":
	# if len(sys.argv) <= 4:
		# print("argumentos: <imagem> <estruturante> <limiar[0,255]> <saida>")
	# if len(sys.argv) <= 3:
	# 	print("argumentos: <imagem> <estruturante> <saida>")
	# 	sys.exit(1)
	
	impath = sys.argv[1]
	# espath = sys.argv[2]
	# limiar = int(sys.argv[3])
	# saida  = sys.argv[4]
	# saida  = sys.argv[3]

	# Carregar ambas imagens em escala de cinza (facilita limiarização)
	img = cv2.imread(impath, 0)
	# est = cv2.imread(espath, 0)

	# cv2.imshow("argh", est)
	# cv2.waitKey()
	# cv2.destroyAllWindows()

	img = limiarizar(img)
	img = fechamento(img, skm.disk(4))
	img = skm.remove_small_holes(img, area_threshold=1024)
	# est = limiarizar(est)
	# est = fechamento(est, skm.disk(30))

	cv2.imwrite("etapas/moedas_limiar.png", toBGR(img))

	# cv2.imshow("argh", toBGR(est))
	# cv2.waitKey()
	# cv2.destroyAllWindows()
	cv2.imshow("argh", toBGR(img))
	cv2.waitKey()
	cv2.destroyAllWindows()

	# op = input("Quer executar:\n [d]ilatação, [e]rosão, [a]bertura ou [f]echamento? ")
	# if op == 'd':
	# 	outimg = dilatacao(img, est)
	# if op == 'e':
	# 	outimg = erosao(img, est)
	# if op == 'a':
	# 	outimg = abertura(img, est)
	# if op == 'f':
	# 	outimg = fechamento(img, est)

	# cv2.imwrite(saida, toBGR(outimg))
