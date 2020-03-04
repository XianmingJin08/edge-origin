import csv
import os
import argparse
import numpy as np
import scipy
from scipy.misc import imread
from scipy.ndimage.morphology import binary_dilation
from scipy.ndimage import generate_binary_structure
from random import random
from random import seed
from PIL import Image
from skimage.color import rgb2gray, gray2rgb

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
            #imsave(img, os.path.join(args.output, file))
            img = scipy.misc.imresize(img,[176,176])
            #imsave(img, os.path.join(args.output, file))
            img = 255 - img
            img = rgb2gray(img)
            img [img>=0.6]=255
            img [img<0.6]=0
            img = img/255
            #imsave(img, os.path.join(args.output, file))
            #img = (img<=255*0.4).astype(np.uint8)*0
            seed(21312)
            num_iterations = int (random()*7)+1
            struct2 = generate_binary_structure(2,2)
            structure=struct2

            img = binary_dilation(img,struct2,num_iterations).astype(np.uint8)*255
            imsave(img, os.path.join(args.output, file))
