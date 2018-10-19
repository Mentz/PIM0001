import numpy as np
import cv2
from matplotlib import pyplot
import sys

img = cv2.imread(sys.argv[1])

# Para histograma em cinza
# fig = pyplot.hist(img.ravel(), 256, [0,256], histtype='step')
# pyplot.xlim([0,256])

# Para histograma RGB
color = ('b', 'g', 'r')
pyplot.figure()
for i,col in enumerate(color):
	histr = cv2.calcHist([img],[i],None,[256],[0,256])
	pyplot.plot(histr, color = ['black', 'blue', 'red'][i])
# pyplot.show()
pyplot.ylim(bottom=0)
pyplot.xlim([0,256])
pyplot.savefig(sys.argv[2])
