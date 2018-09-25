import numpy as np
import cv2
from matplotlib import pyplot
import sys

def printHist(img):
	hist = [0]*256
	k = 0
	for i in xrange(img.shape[0]):
		for j in xrange(img.shape[1]):
			hist[img[i, j]] += 1
	for i in hist:
		if i != 0:
			print("[%s] = %s" % (k, i))
		k += 1

img = cv2.imread(sys.argv[1], 0)
#printHist(img)
pyplot.hist(img.ravel(), 256, [0,256]);
pyplot.show()
