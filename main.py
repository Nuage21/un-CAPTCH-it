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
    new_img = np.zeros((n, m, 3), dtype=np.int)
    for i in range(n):
        for j in range(m):
            (r, g, b, a) = img[i, j]
            new_pixel = (0, 0, 0)  # black
            if (r + g + b) >= 1:
                new_pixel = (1, 1, 1)  # white
            new_img[i, j] = new_pixel
    return new_img


def vectorize_img(img):
    (n, m, t) = img.shape
    vec = np.zeros((1, n * m), dtype=np.int)[0, :]  # a row vector
    p = 0
    for i in range(n):
        for j in range(m):
            pixel = img[i, j]
            color = 1  # 1 = white / 0 = black
            if pixel[0] == 0:  # if pixel is black
                color = 0
            vec[p] = color
            p = p + 1
    return vec


def vecorize_5chars(cap):
    v = np.zeros((1, 180), dtype=np.int)[0, :]
    i = 0
    for c in cap:
        if c.isdigit():
            order = ord(c) - 48
            v[i + order] = 1
            i = i + 36
        else:
            i = i + 10
            c = c.lower()
            order = ord(c) - 97
            v[i + order] = 1
            i = i + 26
    return v


DATA_PATH = './samples/'
samplesFileList = [str(join(DATA_PATH, f)) for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]
samplesText = [(f.split('/')[-1]).split('.')[0] for f in samplesFileList]

captcha = samplesFileList[0]

f = img.imread(captcha)

A = np.random.randint(0, 2, (2, 3, 3))

print(A)

print(vectorize_img(A))

# plt.imshow(newF)
# plt.show()
