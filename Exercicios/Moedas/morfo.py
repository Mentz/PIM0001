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
	out = img < limiar
	return out

def toBGR(img):
	y,x = len(img), len(img[0])
	out = np.zeros((y,x,3), np.uint8)
	for i in range(y):
		for j in range(x):
			out[i][j] = (0,0,0) if img[i][j] == 0 else (255,255,255)
	return out

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

def rotular(label, img, aux, y, x):
	fila = [(y,x)]
	while len(fila) > 0:
		y,x = fila.pop()
		aux[y][x] = label
		# contagem[label] += 1
		''' Acima, direita, abaixo, esquerda '''
		if y > 0:
			if img[y,x] == img[y-1, x] and aux[y-1, x] == -1: fila.append((y-1, x))
		if x < len(img[0]) - 1:
			if img[y,x] == img[y, x+1] and aux[y, x+1] == -1: fila.append((y, x+1))
		if y < len(img) - 1:
			if img[y,x] == img[y+1, x] and aux[y+1, x] == -1: fila.append((y+1, x))
		if x > 0:
			if img[y,x] == img[y, x-1] and aux[y, x-1] == -1: fila.append((y, x-1))

# Essa função faz a contagem do número de elementos contíguos (blobs)
# existentes numa imagem binária e retorna esse valor.
def contaElementos(img):
	y, x = len(img), len(img[0])
	aux = np.zeros((y, x), int)
	aux.fill(-1)
	contador = 0
	# Marcar o que não é fundo
	for i in range(y):
		for j in range(x):
			if img[i][j] == 1 and aux[i][j] == -1:
				contador += 1
				rotular(contador, img, aux, i, j)
	return contador

if __name__ == "__main__":
	# Carregar figura em escala de cinza (facilita limiarização)
	print("Calculando limiarização da imagem")
	impath = "img/moedas.jpg"
	img = cv2.imread(impath, 0)
	img = limiarizar(img)
	img = fechamento(img, skm.disk(4))

	# Esse comando é para preencher buracos internos causados pelo
	# alto brilho em algumas das moedas:
	img = skm.remove_small_holes(img, area_threshold=768)

	cv2.imwrite("etapas/moedas_limiar.png", toBGR(img))

	# cv2.imshow("argh", toBGR(img))
	# cv2.waitKey()
	# cv2.destroyAllWindows()
	
	# Vetor que guardará cada versão filtrada da imagem original
	imff = list()
	# Vetor para armazenar quantidade de moedas detectadas em cada imagem
	imct = list()

	# A ordem de tamanho decrescente das moedas é a seguinte:
	# 100
	# 25-2 (marrom)
	# 25-1 (prata)
	# 50
	# 10-2 (prata)    igual ao 5-2 em tamanho
	# 5-2 (marrom)    igual ao 10-2 em tamanho
	# 5-1 (prata)
	# 10-1 (dourado)

	# Cada elemento estruturante será carregado de maneira similar
	moedas = ["100", "25-2", "25-1", "50", "10-2", "5-2", "5-1", "10-1"]
	for tipo in moedas:
		print("Calculando estruturante da moeda {}".format(tipo))
		espath = "img/m" + tipo + ".png"
		est = cv2.imread(espath, 0)
		est = limiarizar(est)
		est = fechamento(est, skm.disk(3))

		# Esse comando é para preencher buracos internos causados pelo
		# alto brilho em algumas das moedas:
		est = skm.remove_small_holes(est, area_threshold=768)

		# Erosão para reduzir ligeiramente o diâmetro da moeda
		# estruturante, para caso existam outras moedas do mesmo
		# tipo com tamanho ligeiramente diferente na imagem.
		est = erosao(est, skm.diamond(1))

		cv2.imwrite("etapas/est_m{}.png".format(tipo), toBGR(est))

		# Filtra a imagem por elementos iguais ou maiores que o estruturante
		print("Filtrando moedas iguais ou maiores que o tipo {}".format(tipo))
		imget = erosao(img, est)
		# Aqui existem pequenos "blobs" indicando as moedas que foram reconhecidas.
		imff.append(imget)
		# Vamos contar quantos "blobs" existem para obter o número de moedas
		imct.append(contaElementos(imget))
		# .. e descontar dos "blobs" das moedas maiores.
		latest = len(imct) - 1
		for i in range(latest):
			imct[latest] -= imct[i]
		print("Existem {} moedas do tipo {}".format(imct[latest], tipo))

		cv2.imwrite("etapas/im-m{}.png".format(tipo), toBGR(imget))

		# cv2.imshow("argh", toBGR(est))
		# cv2.waitKey()
		# cv2.destroyAllWindows()

	print("Fim! -- Na verdade, falta apresentar o valor das moedas na foto.")
