from src import Taquin
from src import Node

taq = Taquin.Taquin()
taq.generate_random(3)
print(taq)
_, solution = taq.get_solution()
print(_)
print(solution)
n1 = Node.Node(taq, None)
print(n1.get_manhanttan_distance(target=solution))
taq.move_in_place("top")
print(taq)
