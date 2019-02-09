import numpy as np

from . import NodeList

class Node:

    nb_of_node = 0

    def __init__(self, taquin, parent=None, target_taquin=None):
        """
        Create a new node in the graph
        :param taquin: Numpy array of the taquin state at this node
        :param parent: Node object
        :param target_taquin: tacquin to reach, in the form of a dictionary
        """
        self.taquin = taquin
        self.parent = parent
        if isinstance(target_taquin, dict):
            self.end_node = target_taquin
        else:
            raise TypeError("Target taquin shall be given as a dictionary. Got {}.".format(type(target_taquin)))
        self.cost = 0 if not parent else parent.cost + 1
        self.distance = self.get_manhanttan_distance(target_taquin) if target_taquin else 0
        self.heuristic = self.cost + self.distance
        Node.nb_of_node += 1
        self.id = Node.nb_of_node

    def __repr__(self):
        ret = "Node {}:\n".format(self.id)
        ret += str(self.taquin)
        ret += "\ndistance: {} ; cost: {} ; heuristic: {} ; parent: {}".format(
            self.distance, self.cost, self.heuristic, bool(self.parent))
        return ret

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

    def get_manhanttan_distance(self, target=None):
        """
        Compute the manhattan distance from the current node to the target node
        :param target: target node in the from of a dictionary
        :return:
        """
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

    def get_neighbor_node(self):
        """
        Return a list of all neighbors' node. A neighbor is a taquin achievable within 1 move from the current taquin.
        :return: list of neighbors Node object
        """
        moves = ["top", "bottom", "left", "right"]
        neighbors = NodeList.NodeList()
        for move in moves:
            tmp = self.taquin.get_moved_taquin(move)
            if tmp:
                neighbors.append(Node(tmp, parent=self, target_taquin=self.end_node))
        return neighbors

    def get_hamming_distance(self, target=None):
        if not target:
            _, target = self.taquin.get_solution()
        heuristic = 0
        iterator = np.nditer(self.taquin.grid, flags=['multi_index'])
        while not iterator.finished:
            if iterator[0] != 0:
                if target[int(iterator[0])][0] != int(iterator.multi_index[0]):
                    heuristic += 1
                elif target[int(iterator[0])][1] != int(iterator.multi_index[1]):
                    heuristic += 1
            iterator.iternext()
        return heuristic

    def get_euclidian_distance(self, target=None):
        if not target:
            _, target = self.taquin.get_solution()
        heuristic = 0
        iterator = np.nditer(self.taquin.grid, flags=['multi_index'])
        while not iterator.finished:
            if iterator[0] != 0:
                if target[int(iterator[0])][0] != int(iterator.multi_index[0]):
                    heuristic += 1
                elif target[int(iterator[0])][1] != int(iterator.multi_index[1]):
                    heuristic += 1
            iterator.iternext()
        return heuristic

    def get_linear_conflict(self, target=None):
        if not target:
            _, target = self.taquin.get_solution()
        heuristic = self.get_manhanttan_distance(target=target)
        print (heuristic)
        iterator = np.nditer(self.taquin.grid, flags=['multi_index'])
        while not iterator.finished:
            if iterator[0] != 0:
                if target[int(iterator[0])][0] == int(iterator.multi_index[0]):
                    heuristic += 2
                elif target[int(iterator[0])][1] != int(iterator.multi_index[1]):
                    heuristic += 1
            iterator.iternext()
        return heuristic

