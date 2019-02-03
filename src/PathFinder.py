import heapq

from . import NodeList
from . import Node

class PathFinder:

    def __init__(self, start_node):
        self.start_node = start_node
        self.open_list = None
        self.closed_list = None
        self.current_node = None

    def _print_iter(self, cpt):
        print("----------------------------------")
        print("cpt = {}".format(cpt))
        print("opened : [{}]".format(self.open_list))
        print("closed : [{}]".format(self.closed_list))
        print("self.current_node :\n{}".format(self.current_node))

    def a_star(self, verbose=False, heuristic="Manhattan"):
        self.open_list = NodeList.NodeList([self.start_node])
        self.closed_list = NodeList.NodeList()
        cpt = 0
        self.current_node = heapq.heappop(self.open_list)
        while self.current_node.distance > 0 and cpt < 5000:
            cpt += 1
            if verbose:
                self._print_iter(cpt)
            neighbors = NodeList.NodeList([neighbor for neighbor in self.current_node.get_neighbor_node() if neighbor not in self.closed_list])
            heapq.heapify(neighbors)
            self.open_list = NodeList.NodeList(heapq.merge(self.open_list, neighbors))
            self.closed_list.append(self.current_node)
            self.current_node = heapq.heappop(self.open_list)
        print("End!")
        if self.current_node.distance > 0:
            print("No solution found")
            return
        print("Final node")
        print(self.current_node)
        nb_move, solution = self.rewind_play(self.current_node)
        print("\n----------------------------\nPlay:")
        for node in solution:
            print(node)
        print("Solved in {} moves and {} iterations".format(nb_move, cpt))

    def rewind_play(self, last_node):
        play = NodeList.NodeList([last_node])
        nb_move = 0
        while last_node.parent:
            nb_move += 1
            last_node = last_node.parent
            play.append(last_node)
        return nb_move, play
