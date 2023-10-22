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
        
        
    def resize_images(self, img1, img2):
    
        min_width = min(img1.size[0], img2.size[0])
        min_height = min(img1.size[1], img2.size[1])
        
        img1_resized = img1.resize((min_width, min_height))
        img2_resized = img2.resize((min_width, min_height))
        return img1_resized, img2_resized
    
    def blend_bw_images(self, img1, img2, alpha):
    
        blended_img = Image.new("L", img1.size)

        img1_data = img1.load()
        img2_data = img2.load()
        blended_data = blended_img.load()

        for y in range(img1.size[1]):
            for x in range(img1.size[0]):
                p1 = img1_data[x, y]
                p2 = img2_data[x, y]

                p_out = round(p1 * (1 - alpha) + p2 * alpha)

                blended_data[x, y] = p_out

        return blended_img
        
    def blend_color_images(self, img1, img2, alpha):
        blended_img = Image.new("RGBA", img1.size)

        img1_data = img1.load()
        img2_data = img2.load()
        blended_data = blended_img.load()

        for y in range(img1.size[1]):
            for x in range(img1.size[0]):
                r1, g1, b1, a1 = img1_data[x, y]
                r2, g2, b2, a2 = img2_data[x, y]

                r_out = round(r1 * (1 - alpha) + r2 * alpha)
                g_out = round(g1 * (1 - alpha) + g2 * alpha)
                b_out = round(b1 * (1 - alpha) + b2 * alpha)
                a_out = round(a1 * (1 - alpha) + a2 * alpha)

                blended_data[x, y] = (r_out, g_out, b_out, a_out)

        return blended_img
        

    def blend_images(self, img2, alpha):
        if self.img.size != img2.size:
            self.img, img2 = self.resize_images(self.img, img2)
        if self.img.mode == 'L' and img2.mode == 'L':
            return self.blend_bw_images(self.img, img2, alpha)
        else:
            img1 = self.img.convert("RGBA")
            img2 = img2.convert("RGBA")
            return self.blend_color_images(img1, img2, alpha)
            
     def blur_image(self, size):
        if self.img.mode == 'L':
            return self.blur_bw_image(size)
        else:
            return self.blur_color_image(size)


ImageProcess("cow.jpg").show()
