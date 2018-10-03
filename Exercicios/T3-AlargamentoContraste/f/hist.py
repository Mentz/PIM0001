import numpy as np
import cv2
from matplotlib import pyplot
import sys

img = cv2.imread(sys.argv[1], 0)
fig = pyplot.hist(img.ravel(), 256, [0,256]);
pyplot.xlim([0,256])
pyplot.savefig(sys.argv[2])
