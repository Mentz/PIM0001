# Gerador de tabuleiro xadrez
# by: Lucas Litter Mentz

import numpy as np
import cv2
from sys import exit,argv

x, y, l = 10, 10, 2
path = 'garbage'

''' Ler variaveis da linha de comando '''
if len(argv) >= 3:
	path = argv[1]
	r = int(argv[2])
else:
	print("Uso: %s <caminho da imagem> r\n"
		  "    r   Fator de reducao da dimensao da imagem\n"
		  "---- O programa gera um arquivo de saida "
		  "(reduzido.png) no diretorio atual."
		  % argv[0])
	exit(1)	

img = cv2.imread(path)
rimg = img[::r, ::r]

cv2.imwrite('reduzido.png', rimg)
