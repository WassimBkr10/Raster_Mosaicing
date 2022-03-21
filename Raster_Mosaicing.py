from rasterio.plot import show
from rasterio.merge import merge
import rasterio as rio
from pathlib import Path


path = Path('C:\WBK\\NICE_ECW_17092021\\10022022\\_Images\\Nouveau dossier\\')
Path('output').mkdir(parents=True, exist_ok=True)
output_path = 'C:\WBK\\NICE_ECW_17092021\\10022022\\_Images\\Nouveau dossier\\mosaic_output.tif'

raster_files = list(path.iterdir())
raster_to_mosiac = []

for p in raster_files:
    raster = rio.open(p)
    raster_to_mosiac.append(raster)

    mosaic, output = merge(raster_to_mosiac)

    output_meta = raster.meta.copy()
output_meta.update(
    {"driver": "GTiff",
        "height": mosaic.shape[1],
        "width": mosaic.shape[2],
        "transform": output,
     }
)

with rio.open(output_path, 'w', **output_meta) as m:
    m.write(mosaic)



# ______________________________________________________________________________

# import numpy
# import glob
# import cv2
# import csv
# import math
# import os
# import string
# from skimage.color import rgb2gray
# from PIL import Image

# mylist = [f for f in glob.glob("C:\WBK\\NICE_ECW_17092021\\10022022\\_Images\\Nouveau dossier\\mosaic_output.tif")]

# for imagefile in mylist:
#     img_color = cv2.imread(imagefile)
#     image = cv2.resize(img_color,(100,100),interpolation = cv2.INTER_AREA)
#     img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     #img_gray = rgb2gray(image)
#     img_gray.flatten()
#     cv2.imwrite("gray"+imagefile,img_gray)
