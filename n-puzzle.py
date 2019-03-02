import heapq
import numpy as np
import fileinput
import argparse


from timeit import Timer
from src import Node
from src import PathFinder
from src import config

"""
# TEST
start_node = Node.Node(grid=[2, 1, 3, 8, 0, 4, 7, 6, 5], heuristic_fct="linear_conflict")
start_node = Node.Node(grid=[2, 1, 3, 7, 0, 4, 8, 6, 5], heuristic_fct="linear_conflict")
start_node = Node.Node(grid=[2, 1, 3, 7, 6, 4, 8, 0, 5], heuristic_fct="linear_conflict")
start_node = Node.Node(grid=[3, 1, 2, 8, 0, 4, 7, 6, 5], heuristic_fct="linear_conflict")
start_node = Node.Node(grid=[3, 2, 1, 8, 0, 4, 7, 6, 5], heuristic_fct="linear_conflict")
start_node = Node.Node(grid=[1, 2, 5, 8, 0, 4, 7, 6, 3], heuristic_fct="linear_conflict")
start_node = Node.Node(grid=[1, 2, 3, 8, 4, 5, 7, 6, 0], heuristic_fct="linear_conflict")
solution = Node.Node.get_solution()
print(start_node)
start_node.set_target_grid(solution)
print(start_node)
"""



def run(int_lst, heuristic_fct):
    #start_node = Node.Node.generate_random_node()
    #start_node = Node.Node(grid=[8, 3, 4, 2, 1, 5, 7, 6, 0])
    #start_node = Node.Node(grid=[2, 4, 0, 3, 8, 1, 7, 6, 5])
    #start_node = Node.Node(grid=[1, 12, 9, 4, 0, 11, 3, 2, 14, 6, 10, 8, 7, 13, 15, 5])
    #start_node = Node.Node(grid=[1, 2, 3, 4, 12, 13, 14, 5, 11, 9, 15, 6, 10, 8, 0, 7])
    #start_node = Node.Node(grid=[1, 7, 2, 4, 0, 5, 8, 3, 6], heuristic_fct="manhanttan")
    #start_node = Node.Node(grid=[1, 7, 2, 4, 0, 5, 8, 3, 6], heuristic_fct="linear_conflict")
    #start_node = Node.Node(grid=[1, 14, 7, 6, 11, 12, 2, 8, 4, 0, 3, 5, 15, 10, 9, 13], heuristic_fct="linear_conflict")
    #start_node = Node.Node(grid=[1, 10, 2, 3, 0, 12, 14, 8, 9, 13, 4, 6, 11, 15, 7, 5], heuristic_fct="manhanttan")
    #start_node = Node.Node(grid=[1, 10, 2, 3, 0, 12, 14, 8, 9, 13, 4, 6, 11, 15, 7, 5], heuristic_fct="linear_conflict")
    start_node = Node.Node(grid=int_lst, heuristic_fct=heuristic_fct)
    solution = Node.Node.get_solution()
    start_node.set_target_grid(solution)
    print("Start node :")
    print(start_node)
    print("Solution :")
    print(solution)
    algo = PathFinder.PathFinder(start_node=start_node)
    algo.a_star()
    algo.print_solution()
    algo.export_solution("unit_test/solution/{}.pkl".format(start_node.id))

def heuristic_fct(args):
	if args.Manhatan:
		return "manhanttan"
	elif args.Linear_conflict:
		return "linear_conflict"
	elif args.Euclidian:
		return "Euclidian"
	elif args.Hamming_distance:
		return "Hamming_distance"



if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-M', '-Manhatan', dest='Manhatan', action='store_true')
	parser.add_argument('-H', '-Hamming_distance', dest='Hamming_distance', action='store_true')
	parser.add_argument('-L', '-Linear_conflict', dest='Linear_conflict', action='store_true')
	parser.add_argument('-E', '-Euclidian', dest='Euclidian', action='store_true')
	parser.add_argument("files", metavar="file", nargs="*")
	args = parser.parse_args()
	print (args)


	tab = []
	int_lst = []

	for line in fileinput.input(args.files):
		line = line.split('#')
		print(line, end='')
		line[0] = line[0].strip()
		if (line[0].isdigit() and config.TAQUIN_SIZE == 0 and len(line[0])):
			config.TAQUIN_SIZE = int(line[0])
			print("taille taquin : "+ str(config.TAQUIN_SIZE), end='') #taille dans la variable globale config.TAQUIN_SIZE
		else:
			tab = line[0].split(' ')
			print(line[0].split(' '))
			x = 0
			while x in range(len(tab)): #problemme avec for in range et .pop
				if not tab[x]:
					tab.pop(x)
				elif not tab[x].isdigit():
					print ("Not a number")
					exit ()
				elif int(tab[x]) > int(config.TAQUIN_SIZE)**2 - 1:
					print ("number > number Max")
					exit ()
				else:
					x += 1
			print(tab)
			int_lst += [int(x) for x in tab]
			tab = set(tab)
			if (len(tab) != int(config.TAQUIN_SIZE)):
				print ("ne correspond pas a la taille du jeu ou doublon: ", end='')
				print (len(tab), end='=')
				print (config.TAQUIN_SIZE)
				print (tab)
				exit ()
		print("==>", end='')
		print(int_lst)
		pass
	if config.TAQUIN_SIZE == 0:
		print("Error")
		exit ()
	print ()
	print ()
	t = Timer(lambda: run(int_lst, heuristic_fct(args)))
	print("exe time : {}".format(t.timeit(number=1)))
