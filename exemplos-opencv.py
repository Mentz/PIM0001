######################################
# Básico                             #
######################################

import numpy as np
import cv2

img = cv2.imread('lena.png')

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

######################################
# Acessar um pixel                   #
######################################

x, y = 10, 10
b, g, r = img[y, x]
# ou
b,g,r = img[y][x]
print ("(%s, %s), R%s, G%s, B%s" % (x, y, r, g, b))


######################################
# Criar uma imagem 8bits per channel #
######################################

# Cinza
img = np.zeros((500,500), np.uint8)
# RGB
img = np.zeros((500,500,3), np.uint8)


######################################
# Slice NumPy (sel. parte da imagem) #
######################################

img[10:100, 10:100] = 255
img[10:100, 10:100] # Intervalo retangular
img[::, ::] # Seleciona a imagem inteira (:: seleciona todos)
img[::2, ::2] # Selecionar todos (::) pulando de 2 em dois


######################################
# Alterar algo na imagem             #
######################################
img2 = img - 10 # retirar 10 do valor de cor de cada pixel
