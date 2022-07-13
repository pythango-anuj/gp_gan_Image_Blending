import os
import numpy as np
import cv2
import subprocess
#import skimage.draw
import skimage
from skimage import io
import glob

def get_image_after_processing(mask , fg = None , bg = None):
        # fg ---> fore ground
        # bg ---> background
    if mask.shape[-1] > 0:
        mask = (np.sum(mask, -1, keepdims=True) >= 1)
        splash = np.where(mask, bg, fg).astype(np.uint8)
    return splash


def save_image(img_path, img):
    dump_dir = img_path.rsplit("/",1)[0]
    if not os.path.exists(dump_dir):
            subprocess.run("mkdir -p " + dump_dir , shell = True)
    skimage.io.imsave(img_path, img)
    print(" saved image: {}".format(img_path) )

mask_dir="/content/GP-GAN/mask/dentra_masks_/mask/*.npy"
masks = glob.glob(mask_dir)

for mask in masks:
    mask_npy_file = mask 
    bname = os.path.basename(mask_npy_file)
    bname = bname[:-4]
    dump_file = '/content/GP-GAN/mask/dentra_masks/' + bname + '.jpeg'
    maskr = np.load(mask_npy_file)

    img = get_image_after_processing(maskr , fg = 0 ,bg = 255)
    save_image(dump_file, img)
