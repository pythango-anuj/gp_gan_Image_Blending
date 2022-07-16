from __future__ import print_function
from builtins import input
import cv2 as cv
import numpy as np
import argparse
import glob
import os
# Read image given by user
parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.')
parser.add_argument('--input', help='Path to input image.', default='')
args = parser.parse_args()
src_dir= '/content/GP-GAN/DataBase/DentraTrainingData/data/GT/*.jpeg'
images = glob.glob(src_dir)
nf=0
for image in images:
    args.input = image
    image = cv.imread(cv.samples.findFile(args.input))
    if image is None:
        print('Could not open or find the image: ', args.input)
        exit(0)
    new_image = np.zeros(image.shape, image.dtype)
    nf+=1
    os.mkdir(str(nf))
    alpha = 0.5 # Simple contrast control
    beta = 11    # Simple brightness control
    ni=0
    for i in range(10):
        alpha = alpha + 0.1
        if i%4==0:
            beta = beta - 1
        # Do the operation new_image(i,j) = alpha*image(i,j) + beta
        # Instead of these 'for' loops we could have used simply:
        # new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
        # but we wanted to show you how to access the pixels :)
        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                for c in range(image.shape[2]):
                    new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
        ni+=1
        image_file_name = '/content/GP-GAN/DataBase/DentraTrainingData/training_set/'+str(nf)+'/'+str(ni)+'.jpeg'
        cv.imwrite(image_file_name,new_image)
