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
            original_pxl = img.getpixel((x,y))
            result_pxl = int(contrast*original_pxl+brightness)
            if result_pxl < 0:
                result_pxl = 0
            if result_pxl > 255:
                result_pxl = 255
            img_out.putpixel((x,y),result_pxl)
    return(img_out)

def mirror_padding(img_in):
    w, h = img_in.size
    w_new, h_new = w + 2, h + 2
    img_out = Image.new(img_in.mode, (w_new, h_new))
    for x in range(w_new):
        for y in range(h_new):
            if x == 1:
                x1 = 1-x
            elif x == w+1:
                x1 = 2*w-x
            else:
                x1 = x-1
            if y == 1:
                y1 = 1-y
            elif y == h+1:
                y1 = 2*h-y
            else:
                y1 = y-1
            img_out.putpixel((x, y), img_in.getpixel((x1, y1)))
    return img_out

def weighted_sum(img_in,x,y,kernal):
    g = 0
    for i in range(-1,2):
        for j in range(-1,2):
            original_pxl = img_in.getpixel((x+i,y+j))
            g += original_pxl*kernal[1+i,1+j]
    return(int(g))

def mean_filter(img_in,kernal):
    img = mirror_padding(img_in)
    w, h = img.size
    img_out = img_in.copy()
    for y in range(1,h-1):
        for x in range(1,w-1):
            result_pxl = weighted_sum(img,x,y,kernal)
            img_out.putpixel((x-1,y-1),int(result_pxl))
    return img_out

def horizontal_derivative_filter(img_in):
    kernal = np.dot(np.array([[1], [2], [1]]),np.array([[1, 0, -1]]))
    #print(kernal)
    img_out = mean_filter(img_in,kernal)
    return img_out
#horizontal_derivative_filter(img_bw).show()

def vertical_derivative_filter(img_in):
    kernal = np.dot(np.array([[1], [0], [-1]]),np.array([[1, 2, 1]]))
    #print(kernal)
    img_out = mean_filter(img_in,kernal)
    return img_out
#vertical_derivative_filter(img_bw).show()

def derivative_filter(img_in):

    w, h = img_in.size
    img_h = horizontal_derivative_filter(img_in)
    img_v = vertical_derivative_filter(img_in)
    img_out = Image.new(img_in.mode, (w,h))
    for x in range(w):
        for y in range(h):
            pxl_h = img_h.getpixel((x,y))
            pxl_v = img_v.getpixel((x, y))
            pxl = math.sqrt(pxl_h*pxl_h+pxl_v*pxl_v)
            img_out.putpixel((x, y), int(pxl))
    #print(img_out.size)
    return img_out

class ImageProc:

    def __init__(self, filename):
        with Image.open(filename) as img:
            img.load()
        self.img = img
        self.mode = img.mode
        self.w, self.h = img.size

    def contrast_brightness(self, contrast, brightness):
        if self.mode == 'L':
            res_img = contrast_brightness(self.img, contrast, brightness)
        else:
            r, g, b = self.img.split()
            r_res = contrast_brightness(r, contrast, brightness)
            g_res = contrast_brightness(g, contrast, brightness)
            b_res = contrast_brightness(b, contrast, brightness)
            res_img = Image.merge('RGB',(r_res,g_res,b_res))
        return res_img

    def derivative_filter(self):
        if self.mode == 'L':
            res_img = derivative_filter(self.img)
        else:
            r, g, b = self.img.split()
            r_res = derivative_filter(r)
            g_res = derivative_filter(g)
            b_res = derivative_filter(b)
            res_img = Image.merge('RGB',(r_res,g_res,b_res))
        return res_img





img1 = ImageProc("cow.jpg")
#img1.contrast_brightness(50,25).show()
img1.derivative_filter().show()