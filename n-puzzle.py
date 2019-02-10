import heapq
import numpy as np

from src import Taquin
from src import Node
from src import NodeList
from src import PathFinder

#TEST
start_node = Node.Node.generate_random_node()
start_node = Node.Node(grid=[1, 2, 3, 0, 8, 4, 7, 6, 5])
start_node = Node.Node(grid=[1, 7, 2, 4, 0, 5, 8, 3, 6])
start_node = Node.Node(grid=[2, 4, 0, 3, 8, 1, 7, 6, 5])
solution = Node.Node.get_solution()
start_node.set_target_grid(solution)
print(start_node)
print("solution : {}".format(solution))
neighbor = Node.Node.get_neighbor_to(start_node)
for node in neighbor:
    print(node)

"""
init_taquin = Taquin.Taquin(grid=np.array([[8, 3, 4], [2, 1, 5], [7, 6, 0]]))
init_taquin = Taquin.Taquin(grid=np.array([[1, 7, 2], [4, 0, 5], [8, 3, 6]]))
init_taquin = Taquin.Taquin(grid=np.array([[2, 4, 0], [3, 8, 1], [7, 6, 5]]))
solution_node, solution_dic = init_taquin.get_solution()
start_node = _old_Node.Node(taquin=init_taquin, target_taquin=solution_dic)
print("Start node :")
print(start_node)
print("Solution :")
print(solution_node)
print(solution_dic)
algo = PathFinder.PathFinder(start_node=start_node)
algo.a_star()
"""
