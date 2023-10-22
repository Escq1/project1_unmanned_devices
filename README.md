# project1_unmanned_devices

- `__init__(self, filename)`: This is the initializer method for the `ImageProc` class. It takes a string argument `filename` which is the path to the image file. This method loads the image, stores it in the `img` instance variable, and also stores the mode and size of the image, and the separated color channels if the image is in color mode. 

```python
"""
__init__(self, filename)

Initializes an instance of the ImageProc class.

Parameters:
- filename (str): The path to the image file.

Attributes:
- img (Image object): The loaded image.
- mode (str): The mode of the image ('L' for black and white, 'RGB' for color).
- w, h (int, int): The width and height of the image.
- r, g, b (Image object, Image object, Image object): The separated color channels of the image, if the image is in color mode.
"""
```

- `resize_images(self, img1, img2)`: This helper function is used by the `blend_images` function. It takes two `Image` objects as arguments and resizes them to the minimum width and height among the two images. It returns a tuple of the resized images.

```python
"""
resize_images(self, img1, img2)

Resizes two images to the minimum width and height among the two images.

Parameters:
- img1, img2 (Image object, Image object): The two images to resize.

Returns:
- img1_resized, img2_resized (Image object, Image object): The resized images.
"""
```

- `blend_bw_images(self, img1, img2, alpha)`: This helper function is used by the `blend_images` function. It takes two black and white `Image` objects and a float `alpha` as arguments. It blends the two images together based on the `alpha` value and returns the blended image.

```python
"""
blend_bw_images(self, img1, img2, alpha)

Blends two black and white images together based on the alpha value.

Parameters:
- img1, img2 (Image object, Image object): The two black and white images to blend.
- alpha (float): The blending factor. Should be between 0 (only img1 is visible) and 1 (only img2 is visible).

Returns:
- blended_img (Image object): The blended image.
"""
```

- `blend_color_images(self, img1, img2, alpha)`: This helper function is used by the `blend_images` function. It takes two color `Image` objects and a float `alpha` as arguments. It blends the two images together based on the `alpha` value and returns the blended image.

```python
"""
blend_color_images(self, img1, img2, alpha)

Blends two color images together based on the alpha value.

Parameters:
- img1, img2 (Image object, Image object): The two color images to blend.
- alpha (float): The blending factor. Should be between 0 (only img1 is visible) and 1 (only img2 is visible).

Returns:
- blended_img (Image object): The blended image.
"""
```
