import numpy as np


class Node:

    def __init__(self, taquin, parent):
        self.taquin = taquin
        self.parent = parent
        self.cost = 0
        self.distance = 0
        self.heuristic = self.cost + self.distance

    def get_manhanttan_distance(self, target=None):
        if not target:
            _, target = self.taquin.get_solution()
        distance = 0
        iterator = np.nditer(self.taquin.grid, flags=['multi_index'])
        while not iterator.finished:
            if iterator[0] != 0:
                distance += abs(target[int(iterator[0])][0] - int(iterator.multi_index[0]))
                distance += abs(target[int(iterator[0])][1] - int(iterator.multi_index[1]))
            iterator.iternext()
        return distance

"""
    def get_neighbors(self):
        neighbors = node
        return
"""
