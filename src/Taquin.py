import numpy as np


class Taquin:

    def __init__(self, grid=None):
        self.grid = grid
        try:
            self.size = grid.shape[0] if grid else 0
        except AttributeError:
            raise TypeError("{} object was given. {} object constructor only takes object with shape attribute"
                            .format(type(grid), self.__class__.__name__))

    def __repr__(self):
        return str(self.grid)

    def generate_random(self, size):
        self.grid = np.arange(size * size)
        np.random.shuffle(self.grid)
        self.grid = self.grid.reshape((size, size))
        self.size = size

    def get_solution(self):
        x = 0
        xmin = 0
        xmax = self.size - 1
        y = 0
        ymin = 0
        ymax = self.size - 1
        cpt = 1
        dir = 1
        for i in range(self.size * self.size):
            self.grid[x][y] = cpt
            if y == ymin and x < xmax:
                x += 1
            elif x == xmax and y < ymax:
                if dir == 1:
                    ymin += 1
                    dir == 2
                y += 1
            elif y == ymax and x > xmin:
                if dir == 1:
                    ymin += 1
                    dir == 2
                x -= 1
            elif x == xmin and y > ymin:
                y -= 1

            if y == ymin and x < xmax:
                x += 1
            elif x == xmax and y < ymax:
                y += 1
            elif y == ymax and x > xmin:
                x -= 1
            elif x == xmin and y > ymin:
                y -= 1

