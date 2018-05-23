import numpy
import pandas
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from imageio import imread

class Image:
    RED_CONSTANT = 0.2125
    GREEN_CONSTANT = 0.7154
    BLUE_CONSTANT = 0.0721
    rgb_constants = pandas.Series([RED_CONSTANT, GREEN_CONSTANT, BLUE_CONSTANT])

    def __init__(self, image_name):
        self.image = imread(image_name)
        self.original = numpy.copy(self.image)

    def rgb_to_grayscale(self):
        (width, height, layers) = self.image.shape
        self.image = numpy.array([[sum(self.get_pixel_value(x, y) * self.rgb_constants) for y in range(height)] for x in range(width)])
        return self

    def horizontal_flip(self):
        self.image = self.image[::-1,:]
        return self

    def vertical_flip(self):
        self.image = self.image[:,::-1]
        return self

    def reverse_colours(self):
        self.image = 255-self.image[:,:]
        return self

    def reset(self):
        self.image = numpy.copy(self.original)

    def get_pixel_value(self, x, y):
        return pandas.Series(self.image[x, y])

    def show(self):
        plt.imshow(self.image, cmap=cm.Greys_r, aspect='equal')
        plt.show()
