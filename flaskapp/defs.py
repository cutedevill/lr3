import pandas as pd
import numpy as np
import os
import sys
from PIL import Image

from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import matplotlib.pyplot as plt

def BLEND_IMAGES(path, path1, path2, coeffitient):
    image1 = Image.open(path1)
    image2 = Image.open(path2)

    image_box = [[]]*2;
    image_box[0] = np.array(image1)
    image_box[1] = np.array(image2)

    image_blended = (image_box[0]*coeffitient + image_box[1]*(1-coeffitient)).astype('uint8')
    img = Image.fromarray(image_blended, 'RGB')
    img.save(path + 'blended.png')

def GRAPHS(path, root, name):
    from skimage import io
    import matplotlib.pyplot as plt
    image = io.imread(path)

    _ = plt.hist(image.ravel(), bins = 64, color = 'Orange', )
    _ = plt.hist(image[:, :, 0].ravel(), bins = 64, color = 'Red', alpha = 0.7)
    _ = plt.hist(image[:, :, 1].ravel(), bins = 64, color = 'Green', alpha = 0.7)
    _ = plt.hist(image[:, :, 2].ravel(), bins = 64, color = 'Blue', alpha = 0.7)
    _ = plt.xlabel('Intensity Value')
    _ = plt.ylabel('Count')
    _ = plt.legend(['Total', 'Red Channel', 'Green Channel', 'Blue Channel'])
    _ = plt.title(name)

    plt.savefig(root)
