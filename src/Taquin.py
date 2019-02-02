import numpy as np


class Taquin:

    def __init__(self, size=None, file=None):
        """
        Create a Tanquin object either from a file or a random Taquin of size 'size'
        :param size: Size of the Taquin
        :param file: File to read to generate the Taquin
        """
        if bool(size) == bool(file):
            raise AttributeError("One and only one of size and file argument shall be defined. Got size={} ; file={}"
                                 .format(size, file))
        if size:
            self.grid = np.arange(size * size).reshape((size, size))
            np.random.shuffle(self.grid)
        else:
            print("Create Taquin from file not yet available")

    def __repr__(self):
        return str(self.grid)
