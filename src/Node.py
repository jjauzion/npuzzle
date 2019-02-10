import copy

from . import config


class Node:

    @staticmethod
    def xy_to_index(x, y):
        return config.TAQUIN_SIZE * x + y

    @staticmethod
    def index_to_xy(index):
        return index // config.TAQUIN_SIZE, index % config.TAQUIN_SIZE

    @staticmethod
    def get_node_after_move(node, move):
        """
        Return a fresh Node object as a child of the Node in argument and with a grid after the required move
        :param node: Node object
        :param move: required move (see config file for list of moves)
        :return: new Node object, child of the Node given in input ; None if the move is not possible
        """
        move_vect = [0, 0]
        move_vect[0] = -1 if move == config.MOVE_TOP else 1 if move == config.MOVE_BOTTOM else 0
        move_vect[1] = -1 if move == config.MOVE_LEFT else 1 if move == config.MOVE_RIGHT else 0
        if node.empty[0] + move_vect[0] < 0 or node.empty[0] + move_vect[0] >= config.TAQUIN_SIZE:
            return None
        if node.empty[1] + move_vect[1] < 0 or node.empty[1] + move_vect[1] >= config.TAQUIN_SIZE:
            return None
        new_node = Node(grid=copy.copy(node.grid), parent_id=node.id, parent_cost=node.cost, target_grid=node.target)
        new_empty_coord = node.empty[0] + move_vect[0], node.empty[1] + move_vect[1]
        new_node.grid[new_empty_coord[0]][new_empty_coord[1]], new_node.grid[node.empty[0]][node.empty[1]] = \
            0, new_node.grid[new_empty_coord[0]][new_empty_coord[1]]
        new_node.empty = new_empty_coord
        return new_node

    @staticmethod
    def get_neighbor_to(node):
        """
        Return a list of the neighbors of the node given in argument
        :param node: Node object for which we want the neighbors
        :return: list of Node object
        """
        neighbor = []
        for move in config.MOVE_LIST:
            tmp = Node.get_node_after_move(node, move)
            if tmp:
                neighbor.append(tmp)
        return neighbor

    def __init__(self, grid, parent_id=None, parent_cost=0, target_grid=None):
        self.grid = grid
        self.parent_id = parent_id
        self.cost = parent_cost + 1 if parent_id else 0
        self.distance = 0
        self.heuristic = 0
        self.id = "".join(str(elm) for elm in self.grid)
        self.empty = self.grid.index(0)
        if target_grid:
            if not isinstance(target_grid, dict):
                raise TypeError("Target grid shall be given as a dictionary")
            self.target = target_grid
            self.set_heuristic()
        else:
            self.target = None

    def set_manhanttan_distance(self):
        """
        Set the manhattan distance of the current node to the target grid
        """
        for index, value in enumerate(self.grid):
            x, y = self.index_to_xy(index)
            self.distance += abs(self.target[value][0] - x)
            self.distance += abs(self.target[value][1] - y)

    def set_heuristic(self):
        self.set_manhanttan_distance()
        self.heuristic = self.cost + self.distance
