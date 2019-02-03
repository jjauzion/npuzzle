import heapq
import numpy as np

from src import Taquin
from src import Node
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
<<<<<<< HEAD
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


=======
print("current node:")
print(n1)
neighbors = n1.get_neighbor_node()
print("neighbors:")
for node in neighbors:
    print(node)
heapq.heapify(neighbors)
print(neighbors)
new_nei = Node.Node(Taquin.Taquin(grid="random", size=3), end_node=solution_dict).get_neighbor_node()
heapq.heapify(new_nei)
print(new_nei)
open_lst = NodeList.NodeList(heapq.merge(neighbors, new_nei))
print("open_list")
print(open_lst)
new = heapq.heappop(open_lst)
print("new")
print(new)
"""

init_taquin = Taquin.Taquin(grid=np.array([[8, 3, 4], [2, 1, 5], [7, 6, 0]]))
init_taquin = Taquin.Taquin(grid=np.array([[1, 7, 2], [4, 0, 5], [8, 3, 6]]))
init_taquin = Taquin.Taquin(grid=np.array([[2, 4, 0], [3, 8, 1], [7, 6, 5]]))
solution_node, solution_dic = init_taquin.get_solution()
start_node = Node.Node(taquin=init_taquin, end_node=solution_dic)
print("Start node :")
print(start_node)
print("Solution :")
print(solution_node)
print(solution_dic)
algo = PathFinder.PathFinder(start_node=start_node)
algo.a_star()
>>>>>>> 424d9d1a24b01f0f245853579ef5b75dfe028b93
