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
