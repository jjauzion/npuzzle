import numpy as np
from . import config


class Taquin:

    def __init__(self, grid, empty=None):
        """
        Build a Taquin either randomly or from an existing grid.
        :param grid: A numpy.ndarray of the taquin grid
        :param size: if grid == "random", size defines the grid size
        """
        self.grid = grid
        self.empty = self.get_empty_coord() if not empty else empty

    def get_empty_coord(self):
        """
        Search the 0 value in the grid and return a tuple with x and y coordinate of the 0.
        :return: (x, y)
        """
        empty = np.where(self.grid==0)
        empty = int(empty[0]), int(empty[1])
        return empty
