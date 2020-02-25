import csv
import os
import argparse
import numpy as np
import scipy
from scipy.misc import imread
from random import random
from random import seed
from PIL import Image
# pyton reshape.py --path ../edge-connect/celeba/test --output ../edge-connect/celeba_resize/test
def resize(img):
    imgh, imgw = img.shape[0:2]
    side = 178
    j = (imgh - side) // 2
    i = (imgw - side) // 2
    img = img[j:j + side, i:i + side, ...]
    img = scipy.misc.imresize(img, [176, 176])
    return img

def imsave(img, path):
    im = Image.fromarray(img.astype(np.uint8).squeeze())
    im.save(path)

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, help='path to the images')
parser.add_argument('--output', type=str, help='path to the output folder')
args = parser.parse_args()

ext = {'.JPG', '.JPEG', '.PNG', '.TIF', 'TIFF'}

for root, dirs, files in os.walk(args.path):
    print('loading ' + root)
    for file in files:
        if os.path.splitext(file)[1].upper() in ext:
            img = imread(os.path.join(root, file))
            img = resize(img)
            imsave(img, os.path.join(args.output, file))