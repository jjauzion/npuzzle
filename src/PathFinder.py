import heapq

class PathFinder:

    def __init__(self, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node

    def a_star(self, heuristic="Manhattan"):
        self.open_list = []
        self.closed_list = []
