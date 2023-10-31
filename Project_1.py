import math
import random as rnd
import numpy as np
from numpy import random
from PIL import Image, ImageDraw


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
    return img_out

def noise_gaussian(img_in):
    w, h = img_in.size
    img_out = img_in.copy()
    p = int(0.2 * w * h)
    for i in range(p):
        x = rnd.randint(0, w - 1)
        y = rnd.randint(0, h - 1)
        noise_value = random.normal(0, 30)
        original_pxl = img_in.getpixel((x, y))
        result_pxl = original_pxl + noise_value
        img_out.putpixel((x, y), int(result_pxl))
    return img_out

class ImageProc:

    def __init__(self, filename):
        with Image.open(filename) as img:
            img.load()
        self.img = img
        self.mode = img.mode

    def convert(self):
        img_bw = self.img.convert('L')
        img_bw.save("img_bw.jpg")
        return img_bw

    def noise_gaussian(self):
        if self.mode == 'L':
            res_img = noise_gaussian(self.img)
        else:
            r, g, b = self.img.split()
            r_res = noise_gaussian(r)
            g_res = noise_gaussian(g)
            b_res = noise_gaussian(b)
            res_img = Image.merge('RGB', (r_res, g_res, b_res))
        res_img.save("img_noise.jpg")
        return res_img

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
        if self.mode == 'L' and img2.mode == 'L':
            return self.blend_bw_images(self.img, img2, alpha)
        else:
            img1 = self.img.convert("RGBA")
            img2 = img2.convert("RGBA")
            return self.blend_color_images(img1, img2, alpha)

    def blur_bw_image(self, size):
        img_data = self.img.load()

        blurred_img = Image.new("L", self.img.size)
        blurred_data = blurred_img.load()

        for i in range(size // 2, self.img.width - size // 2):
            for j in range(size // 2, self.img.height - size // 2):
                total = 0
                count = 0
                for x in range(i - size // 2, i + size // 2 + 1):
                    for y in range(j - size // 2, j + size // 2 + 1):
                        total += img_data[x, y]
                        count += 1
                blurred_data[i, j] = total // count

        return blurred_img

    def blur_color_image(self, size):
        img_data = self.img.load()

        blurred_img = Image.new("RGB", self.img.size)
        blurred_data = blurred_img.load()

        for i in range(size // 2, self.img.width - size // 2):
            for j in range(size // 2, self.img.height - size // 2):
                r_total = 0
                g_total = 0
                b_total = 0
                count = 0
                for x in range(i - size // 2, i + size // 2 + 1):
                    for y in range(j - size // 2, j + size // 2 + 1):
                        r, g, b = img_data[x, y]
                        r_total += r
                        g_total += g
                        b_total += b
                        count += 1
                blurred_data[i, j] = (r_total // count, g_total // count, b_total // count)

        return blurred_img

    def blur_image(self, size):
        if self.mode == 'L':
            return self.blur_bw_image(size)
        else:
            return self.blur_color_image(size)

    def invert_operator(self):
        w, h = self.img.size
        img_out = Image.new('RGB', (w, h))
        for x in range(w):
            for y in range(h):
                original_pxl = self.img.getpixel((x, y))
                result_pxl = (255 - original_pxl[0], 255 - original_pxl[1], 255 - original_pxl[2])
                img_out.putpixel((x, y), result_pxl)
        return (img_out)

    def invert_bw_operator(self):
        w, h = self.img.size
        img_out = Image.new('L', (w, h))
        for x in range(w):
            for y in range(h):
                original_pxl = self.img.getpixel((x, y))
                result_pxl = 255 - original_pxl
                img_out.putpixel((x, y), result_pxl)
        return (img_out)

    def invert_image(self):
        if self.mode == 'L':
            return self.invert_bw_operator()
        else:
            return self.invert_operator()

    def drow_frame(self, x1, x2, y1, y2):
        w,h = self.img.size
        drow = ImageDraw.Draw(self.img)
        if self.mode == 'L':
            line_color = (0)
        else:
            line_color = (255, 0, 0)
        line_width = 5
        drow.line([(x1, y1), (x1, y2), (x2, y2), (x2, y1), (x1, y1)], fill=line_color, width=line_width)
        self.img.show()


# method checking
img_cow = ImageProc("cow.jpg")
img_cow.convert()
img_cow_bw = ImageProc("img_bw.jpg")
img_cow.noise_gaussian()#.show()
img_cow_noise = ImageProc("img_noise.jpg")
img_cow_bw.noise_gaussian()#.show()
img_cow_bw_noise = ImageProc("img_noise.jpg")

img_monkey = ImageProc("monkey.jpg")
img_monkey.convert()
img_monkey_bw = ImageProc("img_bw.jpg")

img_pig = ImageProc("pig.jpeg")
img_pig.convert()
img_pig_bw = ImageProc("img_bw.jpg")

#img_cow.contrast_brightness(2,-100).show()
#img_cow_bw.contrast_brightness(2,-100).show()

#img_cow.invert_image().show()
#img_cow_bw.invert_image().show()

#img_cow.drow_frame(5,200,5,899)
#img_cow_bw.drow_frame(500,1290,155,899)

#img_cow.blend_images(img_monkey.img,0.5).show()
#img_cow_bw.blend_images(img_monkey_bw.img,0.5).show()
#img_monkey.blend_images(img_cow.img,0.5).show()
#img_monkey_bw.blend_images(img_cow_bw.img,0.5).show()
#img_monkey_bw.blend_images(img_cow.img,0.5).show()
#img_cow.blend_images(img_monkey_bw.img,0.5).show()

#img_cow_noise.blur_image(8).show()
#img_cow_bw_noise.blur_image(8).show()

#img_cow.derivative_filter().show()
#img_cow_bw.derivative_filter().show()




