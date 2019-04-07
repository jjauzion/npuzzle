import heapq
from pathlib import Path
import pickle

from . import Node
from . import lib


class PathFinder:

    def __init__(self, start_node=None):
        self.start_node = start_node
        self.open_list = None
        self.open_list_id = None
        self.closed_list = None
        self.current_node = None
        self.time_complexity = 0
        self.size_complexity = 0
        self.solution = {"nb_move": -1, "play": []}

    def set_start_node(self, start_node):
        solution = Node.Node.get_solution()
        start_node.set_target_grid(solution)
        self.start_node = start_node

    def _print_iter(self):
        print("----------------------------------")
        print("time complexity = {}".format(self.time_complexity))
        print("size complexity = {}".format(self.size_complexity))
        if self.current_node:
            print("distance = {}".format(self.current_node.distance))
        #print("opened : [{}]".format(self.open_list))
        #print("closed : [{}]".format(self.closed_list))
        print("self.current_node :\n{}".format(self.current_node))

    def _get_twin(self, node):
        """
        Search for the node in the closed and open list. Return the existing node if found else return None.
        Return also boolean to indicate if the twin node is in the closed list.
        :param node: node to look for its twin in the closed and open list
        :return: (twin_node, twin_is_in_closed_list(=True or False))
        """
        if node.id in self.closed_list:
            return self.closed_list[node.id], True
        elif node.id in self.open_list_id:
            return self.open_list_id[node.id], False
        return None, False

    def _update_complexity(self, verbose=False):
        self.time_complexity += 1
        if len(self.open_list) > self.size_complexity:
            self.size_complexity = len(self.open_list)
        if verbose and self.time_complexity % verbose == 0:
            self._print_iter()

    def replace_in_open_list(self, node):
        heap_log = [elm.id for elm in self.open_list]
        self.log.append(heap_log)
        node_index = None
        for index, elm in enumerate(self.open_list):
            if elm.id == node.id:
                node_index = index
                break
        if node_index is None:
            raise ValueError("Problem my friend... :/")
        lib.bubble_up(self.open_list, node_index)
        heap_log = [elm.id for elm in self.open_list]
        self.log.append(heap_log)
        self.log.append("------------------")

    def a_star(self, verbose=False):
        """ NEW """
        self.open_list = [self.start_node]
        self.open_list_id = {self.start_node.id: self.start_node}
        self.closed_list = {}
        self.time_complexity = 0
        solution_grid = Node.Node.dico2grid(self.start_node.target)
        solved = False
        self.log = []
        while len(self.open_list) > 0 and not solved:
            if not lib.is_heap(self.open_list, len(self.open_list)):
                raise ValueError("heap is bad...")
            self._update_complexity(verbose)
            self.current_node = heapq.heappop(self.open_list)
            self.open_list_id.pop(self.current_node.id)
            self.closed_list[self.current_node.id] = self.current_node
            if self.current_node.distance == 0 and self.current_node.grid == solution_grid:
                solved = True
            for neighbor in Node.Node.get_neighbor_to(self.current_node):
                twin_node, twin_in_close = self._get_twin(neighbor)
                if twin_node is None:
                    heapq.heappush(self.open_list, neighbor)
                    self.open_list_id[neighbor.id] = neighbor
                elif twin_node.heuristic > neighbor.heuristic:
                    if twin_in_close:
                        heapq.heappush(self.open_list, neighbor)
                        self.open_list_id[neighbor.id] = neighbor
                        self.closed_list.pop(neighbor.id)
                    else:
                        self.replace_in_open_list(neighbor)
        print("final node:\n{}".format(self.current_node))
        print("solution grid:\n{}".format(solution_grid))
        if self.current_node.grid == solution_grid:
            self.solution["nb_move"], self.solution["play"] = self.rewind_play(self.current_node)
        with Path("log_new.txt").open(mode='w', encoding='utf-8') as file:
            for line in self.log:
                file.write("{}\n".format(line))

    def _pop_open_queu(self, node):
        heap_log = [elm.id for elm in self.open_list]
        self.log.append(heap_log)
        for index, open_node in enumerate(self.open_list):
            if open_node.id == node.id:
                self.open_list[index] = self.open_list[-1]
                self.open_list.pop()
                heapq.heapify(self.open_list)
                heap_log = [elm.id for elm in self.open_list]
                self.log.append(heap_log)
                self.log.append("------------------")
                return

    def a_star_old(self, verbose=False):
        """ OLD """
        self.open_list = [self.start_node]
        self.open_list_id = {self.start_node.id: self.start_node}
        self.closed_list = {}
        self.time_complexity = 0
        solution_grid = Node.Node.dico2grid(self.start_node.target)
        solved = False
        self.log = []
        while len(self.open_list) > 0 and not solved:
            if not lib.is_heap(self.open_list, len(self.open_list)):
                raise ValueError("heap is bad...")
            self._update_complexity(verbose)
            self.current_node = heapq.heappop(self.open_list)
            self.open_list_id.pop(self.current_node.id)
            self.closed_list[self.current_node.id] = self.current_node
            if self.current_node.distance == 0 and self.current_node.grid == solution_grid:
                solved = True
            for neighbor in Node.Node.get_neighbor_to(self.current_node):
                twin_node, twin_in_close = self._get_twin(neighbor)
                if twin_node is None:
                    heapq.heappush(self.open_list, neighbor)
                    self.open_list_id[neighbor.id] = neighbor
                elif twin_node.heuristic > neighbor.heuristic:
                    heapq.heappush(self.open_list, neighbor)
                    self.open_list_id[neighbor.id] = neighbor
                    if twin_in_close:
                        self.closed_list.pop(neighbor.id)
                    else:
                        self._pop_open_queu(neighbor)
        if self.current_node.distance == 0:
            self.solution["nb_move"], self.solution["play"] = self.rewind_play(self.current_node)
        with Path("log_old.txt").open(mode='w', encoding='utf-8') as file:
            for line in self.log:
                file.write("{}\n".format(line))

    def print_solution(self):
        print("---------- SOLUTION ----------")
        if self.solution["nb_move"] < 0:
            print("No solution found")
            return
        for node in self.solution["play"]:
            print(node)
        print("Solved in {} moves".format(self.solution["nb_move"]))
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

    def export_solution(self, output_file):
        with Path(output_file).open(mode='wb') as file:
            pickle.dump(self.solution, file)

