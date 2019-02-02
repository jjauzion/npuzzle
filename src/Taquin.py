import numpy as np


class Taquin:

    def __init__(self, grid=np.arange(4).reshape((2, 2))):
        if type(grid) != np.ndarray:
            raise AttributeError("np.ndarray expected for grid argument. Got {} object instead".format(type(grid)))
        self.grid = grid
        self.size = grid.shape[0]
        self.empty = self.get_empty_coord()

    def __repr__(self):
        return str(self.grid)

    def get_empty_coord(self):
        """
        Search the 0 value in the grid and return a tuple with x and y coordinate of the 0.
        :return: (x, y)
        """
        empty = np.where(self.grid==0)
        empty = int(empty[0]), int(empty[1])
        return empty

    def generate_random(self, size):
        """
        Generate a random grid Taquin
        :param size: Size of the Taquin (i.e. taquin will be a grid of size * size)
        :return:
        """
        self.grid = np.arange(size * size)
        np.random.shuffle(self.grid)
        self.grid = self.grid.reshape((size, size))
        self.size = size
        self.empty = self.get_empty_coord()

    def get_moved_taquin(self, move):
        ok_move = ["top", "bottom", "left", "right"]
        if move not in ok_move:
            raise ValueError("Move shall be either {}. Got {}".format(ok_move, move))
        move_vect = [0, 0]
        move_vect[0] = -1 if move == "top" else 1 if move == "bottom" else 0
        move_vect[1] = -1 if move == "left" else 1 if move == "right" else 0
        if self.empty[0] + move_vect[0] < 0 or self.empty[0] + move_vect[0] >= self.size:
            return None
        if self.empty[1] + move_vect[1] < 0 or self.empty[1] + move_vect[1] >= self.size:
            return None
        new_empty_coord = self.empty[0] + move_vect[0], self.empty[1] + move_vect[1]
        tmp = self.grid[new_empty_coord[0]][new_empty_coord[1]]
        self.grid[new_empty_coord[0]][new_empty_coord[1]] = 0
        self.grid[self.empty[0]][self.empty[1]] = tmp
        self.empty = new_empty_coord

    def move_in_place(self, move):
        """
        Apply the required move (top, bottom, left, right) to the taquin and changed its grid
        :param move: Desired move. Choices : "top", "bottom", "left", "right"
        :return:
        """
        ok_move = ["top", "bottom", "left", "right"]
        if move not in ok_move:
            raise ValueError("Move shall be either {}. Got {}".format(ok_move, move))
        move_vect = [0, 0]
        move_vect[0] = -1 if move == "top" else 1 if move == "bottom" else 0
        move_vect[1] = -1 if move == "left" else 1 if move == "right" else 0
        if self.empty[0] + move_vect[0] < 0 or self.empty[0] + move_vect[0] >= self.size:
            return None
        if self.empty[1] + move_vect[1] < 0 or self.empty[1] + move_vect[1] >= self.size:
            return None
        new_empty_coord = self.empty[0] + move_vect[0], self.empty[1] + move_vect[1]
        tmp = self.grid[new_empty_coord[0]][new_empty_coord[1]]
        self.grid[new_empty_coord[0]][new_empty_coord[1]] = 0
        self.grid[self.empty[0]][self.empty[1]] = tmp
        self.empty = new_empty_coord

    def get_solution(self):
        solution = np.zeros((self.size, self.size))
        sol_dict = {}
        y = 0
        ymin = 0
        ymax = self.size - 1
        x= 0
        xmin = 0
        xmax = self.size - 1
        cpt = 1
        dir = 1
        for i in range(self.size * self.size):
            solution[x][y] = cpt
            sol_dict[cpt] = (x, y)
            cpt = cpt + 1 if cpt < self.size * self.size - 1 else 0
            if x == xmin and y < ymax:
                if dir == 4:
                    ymin += 1
                    dir = 1
                y += 1
            elif y == ymax and x < xmax:
                if dir == 1:
                    xmin += 1
                    dir = 2
                x += 1
            elif x == xmax and y > ymin:
                if dir == 2:
                    ymax -= 1
                    dir = 3
                y -= 1
            elif y == ymin and x > xmin:
                if dir == 3:
                    dir = 4
                    xmax -= 1
                x -= 1
        return solution, sol_dict
