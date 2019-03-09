import copy
import random
import math

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
        size = config.TAQUIN_SIZE
        if (move == config.MOVE_LEFT and node.empty % size == 0) or \
                (move == config.MOVE_RIGHT and node.empty % size == size - 1):
            return None
        if (move == config.MOVE_TOP and node.empty // size == 0) or \
                (move == config.MOVE_BOTTOM and node.empty // size == size - 1):
            return None
        move_index = -size if move == config.MOVE_TOP else size if move == config.MOVE_BOTTOM else 0
        move_index += -1 if move == config.MOVE_LEFT else 1 if move == config.MOVE_RIGHT else 0
        new_empty_index = node.empty + move_index
        new_grid = copy.copy(node.grid)
        new_grid[new_empty_index], new_grid[node.empty] = 0, new_grid[new_empty_index]
        return Node(grid=new_grid, parent_id=node.id, parent_cost=node.cost,
                    target_grid=node.target, empty_index=new_empty_index, heuristic_fct=node.heuristic_fct)

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

    @staticmethod
    def generate_random_node():
        return Node(grid=random.sample(range(config.TAQUIN_SIZE ** 2), config.TAQUIN_SIZE ** 2))

    @staticmethod
    def dico2grid(dico):
        """
        transform a taquin given as a dictionary to a grid as a list
        :param dico: dico to transform into a grid
        :return: grid as a List object
        """
        grid = list(range(len(dico)))
        for val in dico:
            index = Node.xy_to_index(dico[val][0], dico[val][1])
            grid[index] = val
        return grid

    @staticmethod
    def get_solution():
        """
        Return the solution of a taquin with size = config.TAQUIN_SIZE
        :return: solution_as_a_dictionary {tile_value: (x, y), ...} eg: {1: (0, 0), 2: (0, 1), ...}
        """
        if config.TAQUIN_SIZE == 1:
            return {0 : (0, 0)}
        solution = {}
        y = 0
        ymin = 0
        ymax = config.TAQUIN_SIZE - 1
        x= 0
        xmin = 0
        xmax = config.TAQUIN_SIZE - 1
        cpt = 1
        dir = 1
        for i in range(config.TAQUIN_SIZE ** 2):
            solution[cpt] = (x, y)
            cpt = cpt + 1 if cpt < config.TAQUIN_SIZE ** 2 - 1 else 0
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
        return solution

    def __init__(self, grid, parent_id=None, parent_cost=0, target_grid=None, empty_index=None, heuristic_fct="manhanttan"):
        self.grid = grid
        self.parent_id = parent_id
        self.cost = parent_cost + 1 if parent_id else 0
        self.distance = 0
        self.heuristic = 0
        self.heuristic_fct = heuristic_fct
        self.id = "".join(str(elm) for elm in self.grid)
        self.empty = self.grid.index(0) if not empty_index else empty_index
        if target_grid:
            if not isinstance(target_grid, dict):
                raise TypeError("Target grid shall be given as a dictionary")
            self.target = target_grid
            self.set_heuristic()
        else:
            self.target = None

    def __repr__(self):
        return "{} ; h={} ; c={} ; d={} ; parent={} ; empty={}".format(
            self.grid, self.heuristic, self.cost, self.distance, self.parent_id, self.empty)

    def __str__(self):
        ret = ""
        for index, nb in enumerate(self.grid):
            if (index + 1) % config.TAQUIN_SIZE == 0:
                ret += "{:<#2}\n".format(nb)
            else:
                ret += "{:<#2} ".format(nb)
        return ret

    def set_manhanttan_distance(self):
        self.distance = 0
        for index, value in enumerate(self.grid):
            if value != 0:
                x, y = self.index_to_xy(index)
                self.distance += abs(self.target[value][0] - x)
                self.distance += abs(self.target[value][1] - y)

    def set_hamming_distance(self):
        self.distance = 0
        for index, value in enumerate(self.grid):
            if value != 0:
                x, y = self.index_to_xy(index)
                if self.target[value][0] != x:
                    self.distance += 1
                elif self.target[value][1] != y:
                    self.distance += 1


    def set_euclidian_distance(self):
        self.distance = 0
        for index, value in enumerate(self.grid):
            if value != 0:
                x, y = self.index_to_xy(index)
                plot1 = [self.target[value][0], self.target[value][1]]
                plot2 = [x, y]
                self.distance += math.sqrt((plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2)

    def set_greedy_search(self):
        self.distance = 99

    def set_uniform_cost(self):
        self.distance = 1

    def set_linear_conflict_distance(self):
        self.set_manhanttan_distance()
        for index, val in enumerate(self.grid):
            x, y = Node.index_to_xy(index)
            target_x, target_y = self.target[val]
            if x != target_x and y != target_y or val == 0:
                continue
            if x == target_x:
                for y_tmp in range(y + 1, target_y + 1):
                    index_tmp = Node.xy_to_index(x, y_tmp)
                    if self.grid[index_tmp] != 0 and self.target[self.grid[index_tmp]][0] == x and \
                            self.target[self.grid[index_tmp]][1] <= target_y:
                        self.distance += 2
            elif y == target_y:
                for x_tmp in range(x + 1, target_x + 1):
                    index_tmp = Node.xy_to_index(x_tmp, y)
                    if self.grid[index_tmp] != 0 and self.target[self.grid[index_tmp]][1] == y and \
                            self.target[self.grid[index_tmp]][0] <= target_x:
                        self.distance += 2

    def __eq__(self, other):
        return self.heuristic == other.heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic

    def __gt__(self, other):
        return self.heuristic > other.heuristic

    def __ge__(self, other):
        return self.heuristic >= other.heuristic

    def __le__(self, other):
        return self.heuristic <= other.heuristic

    def set_heuristic(self):
        if self.heuristic_fct == "manhanttan":
            self.set_manhanttan_distance()
        elif self.heuristic_fct == "linear_conflict":
            self.set_linear_conflict_distance()
        elif self.heuristic_fct == "hamming_distance":
            self.set_hamming_distance()
        elif self.heuristic_fct == "euclidian":
            self.set_euclidian_distance()
        elif self.heuristic_fct == "greedy_search":
            self.set_greedy_search()
        elif self.heuristic_fct == "uniform_cost":
            self.set_uniform_cost()
        else:
            print("{} is not a valid heuristic.".format(self.heuristic))
            exit(1)
        self.heuristic = self.cost + self.distance

    def set_target_grid(self, target):
        if not isinstance(target, dict):
            raise TypeError("Target grid shall be given as a dictionary")
        self.target = target
        self.set_heuristic()