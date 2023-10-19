import math
import random as rnd
import numpy as np
from numpy import random
from PIL import Image

class ImageProcess:

    def open_image(filename):
        with Image.open(filename) as img:
            img.load()

    def linear_operator(img_in, contrast, brightness):
        r, g, b = img.split()
        w,h = img_in.size
        img_out = Image.new('RGB', (w,h))
        for x in range(w):
            for y in range(h):
                pxl_r = r.getpixel((x,y))
                result_pxl = int(contrast*original_pxl+brightness)
                    if result_pxl < 0:
                        result_pxl = 0
                    if result_pxl > 255:
                        result_pxl = 255
                img_out.putpixel((x,y),result_pxl)
    return(img_out)
    

    