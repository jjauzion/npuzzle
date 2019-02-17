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

    def _get_twin(self, node):
        """
        Search for the node in the closed and open list. Return the existing node if found else return None.
        Return also boolean to indicate if the twin node is in the closed list.
        :param node: node to look for its twin in the closed and open list
        :return: (twin_node, twin_is_in_closed_list(=True or False))
        """
        if node.id in self.closed_list:
            return self.closed_list[node.id], True
        else:
            for node_open in self.open_list:
                if node.id == node_open.id:
                    return node_open, False
        return None, False

    def _update_complexity(self, verbose=False):
        self.time_complexity += 1
        if len(self.open_list) > self.size_complexity:
            self.size_complexity = len(self.open_list)
        if verbose:
            self._print_iter()

    def a_star(self, verbose=False, heuristic="Manhattan"):
        self.open_list = [self.start_node]
        self.closed_list = {}
        self.time_complexity = 0
        while len(self.open_list) > 0:
            self._update_complexity(verbose)
            self.current_node = heapq.heappop(self.open_list)
            self.closed_list[self.current_node.id] = self.current_node
            if self.current_node.distance == 0:
                break
            for neighbor in Node.Node.get_neighbor_to(self.current_node):
                twin_node, twin_in_close = self._get_twin(neighbor)
                if twin_node is None:
                    heapq.heappush(self.open_list, neighbor)
                elif twin_node.heuristic > neighbor.heuristic:
                    heapq.heappush(self.open_list, neighbor)
                    if twin_in_close:
                        self.closed_list.pop(neighbor.id)
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
        print("Solved in {} moves".format(nb_move))
        print("Time complexity = {}".format(self.time_complexity))
        print("Size complexity = {}".format(self.size_complexity))

    def rewind_play(self, last_node):
        play = [last_node]
        nb_move = 0
        while last_node.parent_id:
            nb_move += 1
            last_node = self.closed_list[last_node.parent_id]
            play.insert(0, last_node)
        return nb_move, play
