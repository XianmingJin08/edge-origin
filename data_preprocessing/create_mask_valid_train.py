import csv
import os
import argparse
import numpy as np
from random import random
from random import seed

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, help='path to the dataset')
parser.add_argument('--output', type=str, help='path to the file list')
args = parser.parse_args()

train_set_num = 0
eval_set_num = 0

with open('../edge-connect/list_eval_partition.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['partition'] == '0':
            train_set_num += 1
        if row['partition'] == '1':
            eval_set_num += 1
print(train_set_num)
print(eval_set_num)

ext = {'.JPG', '.JPEG', '.PNG', '.TIF', 'TIFF'}

images = []
length = 0
for root, dirs, files in os.walk(args.path):
    print('loading ' + root)
    for file in files:
        length += 1
        if os.path.splitext(file)[1].upper() in ext:
            images.append(os.path.join(root, file))
print(length)
seed(21312)
selected_images = []
for i in range(0, train_set_num):
    selected_images.append(images[int(random() * length)])
np.savetxt(args.output+'_train.flist', selected_images, fmt='%s')

selected_images = []
for i in range(0, eval_set_num):
    selected_images.append(images[int(random() * length)])
np.savetxt(args.output+'_eval.flist', selected_images, fmt='%s')
