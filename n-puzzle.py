import heapq
import numpy as np
import fileinput

from src import Node
from src import PathFinder

"""
#TEST
start_node = Node.Node.generate_random_node()
start_node = Node.Node(grid=[2, 4, 0, 3, 8, 1, 7, 6, 5])
start_node = Node.Node(grid=[1, 7, 2, 4, 0, 5, 8, 3, 6])
solution = Node.Node.get_solution()
start_node.set_target_grid(solution)
print(start_node)
print("solution : {}".format(solution))
neighbor = Node.Node.get_neighbor_to(start_node)
for node in neighbor:
    print(node)
for i in range(5):
    new_node = Node.Node.generate_random_node()
    new_node.set_target_grid(solution)
    neighbor.append(new_node)
best_node = Node.Node(grid=[1, 2, 3, 0, 8, 4, 7, 6, 5])
best_node.set_target_grid(solution)
neighbor.append(best_node)
print("-----------------------------")
for node in neighbor:
    print(node)
heapq.heapify(neighbor)
print("-------AFTER HEAPIFY---------")
for node in neighbor:
    print(node)
"""


def run():
    start_node = Node.Node.generate_random_node()
    start_node = Node.Node(grid=[8, 3, 4, 2, 1, 5, 7, 6, 0])
    start_node = Node.Node(grid=[2, 4, 0, 3, 8, 1, 7, 6, 5])
    start_node = Node.Node(grid=[1, 7, 2, 4, 0, 5, 8, 3, 6])
    solution = Node.Node.get_solution()
    start_node.set_target_grid(solution)
    print("Start node :")
    print(start_node)
    print("Solution :")
    print(solution)
    algo = PathFinder.PathFinder(start_node=start_node)
    algo.a_star()


if __name__ == '__main__':
    from timeit import Timer
    t = Timer(lambda: run())
    print("exe time : {}".format(t.timeit(number=1)))
