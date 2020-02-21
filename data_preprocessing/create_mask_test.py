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

test_set_num = 0

with open('../edge-connect/list_eval_partition.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['partition'] == '2':
            test_set_num += 1

ext = {'.JPG', '.JPEG', '.PNG', '.TIF', 'TIFF'}

images = []
for root, dirs, files in os.walk(args.path):
    print('loading ' + root)
    for file in files:
        if os.path.splitext(file)[1].upper() in ext:
            images.append(os.path.join(root, file))

seed(21312)
selected_images = []
for i in range(0, test_set_num):
    selected_images.append(images[int(random() * 12000)])
print(test_set_num)
np.savetxt(args.output, selected_images, fmt='%s')
