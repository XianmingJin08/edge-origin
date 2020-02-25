import csv
import os
import argparse
import numpy as np
import scipy
from scipy.misc import imread
from random import random
from random import seed
from PIL import Image
from skimage.color import rgb2gray, gray2rgb
# python ./data_preprocessing/reshape.py --path ../edge-connect/data/celeba/test --output ../edge-connect/celeba_resize/test

def imsave(img, path):
    im = Image.fromarray(img.astype(np.uint8).squeeze())
    im.save(path)
    
def binarize(img):
    img = rgb2gray(img)
    img = (img >)

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, help='path to the mask')
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