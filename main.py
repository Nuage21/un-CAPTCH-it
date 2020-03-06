from sklearn import neural_network as nn
from scipy import misc
from matplotlib import pyplot as plt
import numpy as np

from os import listdir
from os.path import isfile, join


DATA_PATH = './samples/'
samplesFileList = [join(DATA_PATH, f) for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]

captcha = samplesFileList[0]

f = plt.imread(captcha)

plt.imshow(f)

plt.show()





