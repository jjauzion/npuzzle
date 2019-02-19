import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-M', '-Manhatan', dest='Manhatan', action='store_true')
	parser.add_argument('-H', '-Hamming_distance', dest='Hamming_distance', action='store_true')
	parser.add_argument('-L', '-Linear_conflict', dest='Linear_conflict', action='store_true')
	parser.add_argument('-E', '-Euclidian', dest='Euclidian', action='store_true')
	args = parser.parse_args()

	print (args)
	print (args.Euclidian)
	print (args.Manhatan)