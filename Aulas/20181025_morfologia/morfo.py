#!/usr/env/python3
#! - coding: UTF8 -

from matplotlib import pyplot
import skimage.morphology as skm
import skimage.filters as skf
import sys
import numpy as np
import cv2

# def limiarizar(img, limiar):
def limiarizar(img):
	limiar = skf.threshold_otsu(img)
	out = img <= limiar

	return out


# NÃO PRECISA IMPLEMENTAR DILATAÇÃO E EROSÃO
# O objetivo é usar abertura e fechamento para contagem
# de moedas em uma foto que está no seu celular, Mentz!
# Biblioteca:
# pymorph ou skimage
# Usar limiarização de OTSU

def dilatacao(img, est):
	# out = img.copy()
	# iy, ix, ey, ex = len(img), len(img[0]), len(est), len(est[0])
	# mey, mex = ey//2, ex//2
	# ddy = range(-mey, ey - mey)
	# ddx = range(-mex, ex - mex)

	# for y in range(mey, iy-(ey - mey)):
	#     for x in range(mex, ix-(ex - mex)):
	#         for dy in ddy:
	#             for dx in ddx:
	#                 if est[mey - dy][mex - dx] == 255:
	#                     if img[y - dy][x - dx] != 255:
	#                         out[y][x] = 0
	#                         break
	out = skm.binary_dilation(img, est)
	return out

def erosao(img, est):
	# out = img.copy()
	# iy, ix, ey, ex = len(img), len(img[0]), len(est), len(est[0])
	# mey, mex = ey//2, ex//2
	# ddy = range(-mey, ey - mey)
	# ddx = range(-mex, ex - mex)

	# for y in range(mey, iy-(ey - mey)):
	#     for x in range(mex, ix-(ex - mex)):
	#         for dy in ddy:
	#             for dx in ddx:
	#                 if est[mey - dy][mex - dx] == 255:
	#                     if img[y - dy][x - dx] != 255:
	#                         out[y][x] = 0
	#                         break
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
	if len(sys.argv) <= 4:
		# print("argumentos: <imagem> <estruturante> <limiar[0,255]> <saida>")
		print("argumentos: <imagem> <estruturante> <saida>")
		sys.exit(1)
	
	impath = sys.argv[1]
	espath = sys.argv[2]
	# limiar = int(sys.argv[3])
	# saida  = sys.argv[4]
	saida  = sys.argv[3]

	# Carregar ambas imagens em escala de cinza (facilita limiarização)
	img = cv2.imread(impath, 0)
	est = cv2.imread(espath, 0)

	img = limiarizar(img)
	est = limiarizar(est)

	op = input("Quer executar:\n [d]ilatação, [e]rosão, [a]bertura ou [f]echamento? ")
	if op == 'd':
		outimg = dilatacao(img, est)
	if op == 'e':
		outimg = erosao(img, est)
	if op == 'a':
		outimg = abertura(img, est)
	if op == 'f':
		outimg = fechamento(img, est)
	
	cv2.imwrite(saida, outimg)