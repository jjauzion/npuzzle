import fileinput
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-M', '-Manhatan', dest='Manhatan', action='store_true')
parser.add_argument('-H', '-Hamming_distance', dest='Hamming_distance', action='store_true')
parser.add_argument('-L', '-Linear_conflict', dest='Linear_conflict', action='store_true')
parser.add_argument('-E', '-Euclidian', dest='Euclidian', action='store_true')
parser.add_argument("files", metavar="file", nargs="*")
args = parser.parse_args()

size = 0
tab = ()
int_lst = []

for line in fileinput.input(args.files):
	line = line.split('#')
	print(line, end='')
	line[0] = line[0].strip()
	if (line[0].isdigit() and size == 0 and len(line[0])):
		size = line[0]
		print("taille taquin : "+ size, end='') #taille dans la variable globale size
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
			elif int(tab[x]) > int(size)**2 - 1:
				print ("number > number Max")
				exit ()
			else:
				x += 1
		print(tab)
		if (len(tab) != int(size)):
			print ("ne correspond pas a la taille du jeu: ", end='')
			print (len(tab), end='=')
			print (size)
			print (tab)
		int_lst += [int(x) for x in tab]
		print("==>", end='')
	print(int_lst)
	pass
