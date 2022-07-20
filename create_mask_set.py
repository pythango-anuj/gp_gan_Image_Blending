import glob
import os
import shutil

src_dir = '/content/GP-GAN/mask/dentra_masks/*.jpeg'
dst_dir = '/content/GP-GAN/mask/cropped_masks/'
images = glob.glob(src_dir)

i=0
for image in images:
  i+=1
  if i>151:
    break
  os.mkdir(str(i))
  copy_dir = dst_dir+str(i)
  shutil.copy(image, copy_dir)
  

