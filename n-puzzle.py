from src import Taquin
from src import Node

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
print("Distance to solution")
print(n1.get_manhanttan_distance(target=solution_dict))
neighbors = n1.get_neighbors()
print("Neigbors")
for neighbor in neighbors:
    print(neighbor)
print("current node:")
print(n1)
n2 = Node.Node(Taquin.Taquin(grid="random", size=3), end_node=solution_dict, parent=n1)
print(n2)
print("n1 >= n2 ? {}".format(n1 >= n2))
