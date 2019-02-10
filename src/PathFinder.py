import heapq

from . import Node
from . import config


class PathFinder:

    def __init__(self, start_node):
        if config.TAQUIN_SIZE ** 2 != len(start_node.grid):
            print("CONFIG ERROR : Taquin size from config file (={}) mismatch with start node grid size (=sqrt({}))"
                  .format(config.TAQUIN_SIZE, len(start_node.grid)))
            exit(1)
        self.start_node = start_node
        self.open_list = None
        self.closed_list = None
        self.current_node = None
        self.time_complexity = 0
        self.size_complexity = 0

    def _print_iter(self):
        print("----------------------------------")
        print("time complexity = {}".format(self.time_complexity))
        print("size complexity = {}".format(self.size_complexity))
        print("opened : [{}]".format(self.open_list))
        print("closed : [{}]".format(self.closed_list))
        print("self.current_node :\n{}".format(self.current_node))
        input("press any key to continue")

    def a_star(self, verbose=False, heuristic="Manhattan"):
        self.open_list = []
        self.closed_list = {}
        self.time_complexity = 0
        self.current_node = self.start_node
        while self.current_node.distance > 0 and self.time_complexity < 15000:
            self.time_complexity += 1
            if len(self.open_list) > self.size_complexity:
                self.size_complexity = len(self.open_list)
            if verbose:
                self._print_iter()
            neighbors = [neighbor for neighbor in Node.Node.get_neighbor_to(self.current_node) if neighbor.id not in self.closed_list]
            heapq.heapify(neighbors)
            self.open_list = list(heapq.merge(self.open_list, neighbors))
            self.closed_list[self.current_node.id] = self.current_node
            self.current_node = heapq.heappop(self.open_list)
        print("End!")
        self.closed_list[self.current_node.id] = self.current_node
        if self.current_node.distance > 0:
            print("No solution found")
            return
        print("Final node")
        print(self.current_node)
        nb_move, solution = self.rewind_play(self.current_node)
        print("\n----------------------------\nPlay:")
        for node in solution:
            print(node)
        print("Solved in {} moves".format(nb_move))
        print("Time complexity = {}".format(self.time_complexity))
        print("Size complexity = {}".format(self.size_complexity))

    def rewind_play(self, last_node):
        play = [last_node]
        nb_move = 0
        while last_node.parent_id:
            nb_move += 1
            last_node = self.closed_list[last_node.parent_id]
            play.append(last_node)
        return nb_move, play
