# Gerador de tabuleiro xadrez
# by: Lucas Litter Mentz

import numpy as np
import cv2
from sys import exit,argv

x, y, l = 10, 10, 2

''' Ler variaveis da linha de comando '''
if len(argv) >= 4:
	x = int(argv[1])
	y = int(argv[2])
	l = int(argv[3])
elif len(argv) >= 3:
	x = int(argv[1])
	y = int(argv[2])
else:
	print("Uso: %s x y l\n"
		  "    x   Largura da imagem gerada\n"
		  "    y   Altura da imagem gerada\n"
		  "    l   Lado de cada quadrado xadrez\n"
		  "---- O programa gera um arquivo de saida "
		  "(checker.png) no diretorio atual."
		  % argv[0])
	exit(1)

img = np.zeros((y, x), np.uint8)
for i in xrange(0, y, l):
	for j in xrange(0, x, l):
		if (((i//l)+(j//l))%2) == 0:
			img[i:i+l, j:j+l] = 255

cv2.imwrite('checker.png', img)
