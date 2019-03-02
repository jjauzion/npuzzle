import heapq
import numpy as np
import fileinput
import argparse


from timeit import Timer
from src import Node
from src import PathFinder
from src import parser
from src import solvability


def run(grid, heuristic_fct):
    start_node = Node.Node(grid=grid, heuristic_fct=heuristic_fct)
    solution = Node.Node.get_solution()
    start_node.set_target_grid(solution)
    print("Start node :")
    print(start_node)
    solvable = solvability.is_solvable(start_node)
    if not solvable:
        print("Puzzle is not solvable")
    else:
        print("Puzzle is solvable")
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
