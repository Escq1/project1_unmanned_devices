import math
import random as rnd
import numpy as np
from numpy import random
from PIL import Image


def contrast_brightness(img, contrast, brightness):
    w,h = img.size
    img_out = Image.new('L', (w,h))
    for x in range(w):
        for y in range(h):
            original_pxl = img_in.getpixel((x,y))
            result_pxl = int(contrast*original_pxl+brightness)
            if result_pxl < 0:
                result_pxl = 0
            if result_pxl > 255:
                result_pxl = 255
            img_out.putpixel((x,y),result_pxl)
    return(img_out)




class ImageProc:

    def __init__(self, filename):
        with Image.open(filename) as img:
            img.load()
        self.img = img
        self.mode = img.mode
        self.w, self.h = img.size
        self.r, self.g, self.b = img.split()

    def contrast_brightness(self, contrast, brightness):
        if self.mode == 'L':
            res_img = contrast_brightness(self.img, contrast, brightness):
        else:
            r, g, b = self.split()
            r_res = contrast_brightness(self.img, contrast, brightness):
            g_res = contrast_brightness(self.img, contrast, brightness):
            b_res = contrast_brightness(self.img, contrast, brightness):
            res_img = Image.merge('RGB',(r_res,g_res,b_res))
        return res_img



ImageProcess("cow.jpg").show()