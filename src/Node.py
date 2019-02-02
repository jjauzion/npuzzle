class Node:

    def __init__(self, taquin, parent):
        self.taquin = taquin
        self.parent = parent
        self.cost = 0
        self.distance = 0
        self.heuristic = self.cost + self.distance
