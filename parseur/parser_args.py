import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-M', '-Manhatan', dest='Manhatan', action='store_true')
	parser.add_argument('-H', '-Hamming_distance', dest='Hamming_distance', action='store_true')
	parser.add_argument('-L', '-Linear_conflict', dest='Linear_conflict', action='store_true')
	parser.add_argument('-E', '-Euclidian', dest='Euclidian', action='store_true')
	args = parser.parse_args()

	a = 0;
	for x in range(4):
		if x == True:
			a += 1

	print (args)
	print (a)