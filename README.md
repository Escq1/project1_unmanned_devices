# project1_unmanned_devices

This Project contains a Python class ImageProc that provides various image processing functionalities. The class is designed to work with images in both black and white and color formats.

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


- `blend_images(self, img2, alpha)`: This method takes an `Image` object and a float `alpha` as arguments. It checks if the image is black and white or color and calls the respective helper function to blend the images. It returns the blended image.

```python
"""
blend_images(self, img2, alpha)

Blends the image associated with the ImageProc instance with another image.

Parameters:
- img2 (Image object): The image to blend with.
- alpha (float): The blending factor. Should be between 0 (only the image associated with the ImageProc instance is visible) and 1 (only img2 is visible).

Returns:
- blended_img (Image object): The blended image.
"""
```

- `blur_bw_image(self, size)`: This helper function is used by the `blur_image` function. It takes an integer `size` as argument. It applies a moving average filter of the given size to the black and white image and returns the blurred image.

```python
"""
blur_bw_image(self, size)

Applies a moving average filter of the given size to the black and white image associated with the ImageProc instance.

Parameters:
- size (int): The size of the moving average window. Should be an odd number.

Returns:
- blurred_img (Image object): The blurred image.
"""
```


- `blur_color_image(self, size)`: This helper function is used by the `blur_image` function. It takes an integer `size` as argument. It applies a moving average filter of the given size to each color channel of the image and returns the blurred image.

```python
"""
blur_color_image(self, size)

Applies a moving average filter of the given size to each color channel of the image associated with the ImageProc instance.

Parameters:
- size (int): The size of the moving average window. Should be an odd number.

Returns:
- blurred_img (Image object): The blurred image.
"""
```

- `blur_image(self, size)`: This method takes an integer `size` as argument. It checks if the image is black and white or color and calls the respective helper function to blur the image. It returns the blurred image.

```python
"""
blur_image(self, size)

Applies a moving average filter of the given size to the image associated with the ImageProc instance.

Parameters:
- size (int): The size of the moving average window. Should be an odd number.

Returns:
- blurred_img (Image object): The blurred image.
"""
```



- `invert_operator(self)`: This function takes an image as input. The function works by iterating through each pixel in the input image and calculating the inverse of the RGB color values. A new image with inverted colors is returned.

```python
"""
invert_operator(self)

A new image is created the same size as the input image, but with the color mode "RGB". All pixels of the input image are iterated. For each pixel we get the original color. The inverted color is calculated by subtracting each color channel from 255. This replaces dark colors with light ones.

Parameters:
- This function only takes an image as input.

Returns:
- invert_img (Image object): Inverted image.
"""
```

- `invert_bw_operator(self)`: This method inverts the colors of an image by changing each pixel of the image to its negative, where the colors are replaced with their opposite values. A new image with inverted colors is returned.

```python
"""
invert_bw_operator(self)

This method creates a negative black and white image by inverting the brightness of all its pixels.

Parameters:
- This function only takes an image as input.

Returns:
- invert_img (Image object): Inverted image.
"""
```

- `invert_image(self)`: This function takes an image as input. It checks if the image is black and white or color and calls the respective helper function. A new image with inverted colors is returned.

```python
"""
invert_image(self)

This method inverts the colors of an image, changing each pixel of the image to its negative.

Parameters:
- This function only takes an image as input.

Returns:
- invert_img (Image object): Inverted image.
"""
```

- `drow_frame(self, x1, x2, y1, y2)`: This method takes four values, which are the coordinates of points, and selects the desired area by drawing lines. The original image with the constructed frame is returned.

```python
"""
drow_frame(self, x1, x2, y1, y2)

Selects a frame using four points (builds a frame).

Parameters:
- x1 (int), x2 (int), y1 (int), y2 (int): Four values that are the coordinates of the four points along which the frame is constructed.

Returns:
- drow_frame (Image object): Image with frame.
"""
```