import heapq
import numpy as np

from src import Taquin
from src import _old_Node
from src import NodeList
from src import PathFinder

"""
TEST
taq = Taquin.Taquin()
taq.generate_random(3)
print("Initial taquin:")
print(taq)
solution_grid, solution_dict = taq.get_solution()
print("Solution taquin:")
print(solution_grid)
print("Solution as a dictionary")
print(solution_dict)
n1 = Node.Node(taq, parent=None, end_node=solution_dict)
print("Manhantan Distance to solution")
print(n1.get_manhanttan_distance(target=solution_dict))
print("Hamming Distance to solution")
print(n1.get_hamming_distance(target=solution_dict))
print("linear conflict to solution")
print(n1.get_linear_conflict(target=solution_dict))
print("Euclidian Distance to solution")
print(n1.get_euclidian_distance(target=solution_dict))
neighbors = n1.get_neighbors()
print("Neigbors")
for neighbor in neighbors:
    print(neighbor)
print("current node:")
print(n1)
n2 = Node.Node(Taquin.Taquin(grid="random", size=3), end_node=solution_dict, parent=n1)
print(n2)
print("n1 >= n2 ? {}".format(n1 >= n2))
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
