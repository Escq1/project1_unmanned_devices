import math
import random as rnd
import numpy as np
from numpy import random
from PIL import Image

class ImageProcess:

    def open_image(filename):
        with Image.open(filename) as img:
            img.load()

    