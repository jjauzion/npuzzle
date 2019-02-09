class Node:

    def __init__(self, grid, parent_id=None):
        self.grid = []
        self.parent_id = parent_id
        self.cost = 0
        self.distance = 0
        self.heuristic = 0
        self.id = "".join(str(elm) for elm in self.grid)
