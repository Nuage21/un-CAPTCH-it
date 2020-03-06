from sklearn import neural_network as nn
import scipy.misc as misc
from matplotlib import pyplot as plt
from matplotlib import image as img
import numpy as np
import scipy.ndimage as ndi

from os import listdir
from os.path import isfile, join


def bwof(img):  # return img as black-white
    (n, m, t) = img.shape
    new_img = np.zeros((n, m, 3))
    for i in range(n):
        for j in range(m):
            (r, g, b, a) = img[i, j]
            new_pixel = (0, 0, 0)  # black
            if (r + g + b) >= 1:
                new_pixel = (1, 1, 1)  # white
            new_img[i, j] = new_pixel
    return new_img


DATA_PATH = './samples/'
samplesFileList = [str(join(DATA_PATH, f)) for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]
samplesText = [(f.split('/')[-1]).split('.')[0] for f in samplesFileList]

captcha = samplesFileList[0]

f = img.imread(captcha)

newF = bwof(f)

print(newF[0, 0])

plt.imshow(newF)

plt.show()
