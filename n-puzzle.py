import argparse
from timeit import Timer

from src import Node
from src import PathFinder
from src import parser

def run(int_lst, heuristic_fct):
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
    #algo.export_solution("unit_test/solution/{}.pkl".format(start_node.id))


def heuristic_fct(args):
    if args.Linear_conflict:
        return "linear_conflict"
    elif args.Euclidian:
        return "Euclidian"
    elif args.Hamming_distance:
        return "Hamming_distance"
    else:
        return "manhanttan"


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-M', '-Manhatan', dest='Manhatan', action='store_true')
    arg_parser.add_argument('-H', '-Hamming_distance', dest='Hamming_distance', action='store_true')
    arg_parser.add_argument('-L', '-Linear_conflict', dest='Linear_conflict', action='store_true')
    arg_parser.add_argument('-E', '-Euclidian', dest='Euclidian', action='store_true')
    arg_parser.add_argument('-T', '-Timer', action='store_true', help="print total execution time")
    arg_parser.add_argument("files", metavar="file", nargs="*", help="input file with a puzzle")
    args = arg_parser.parse_args()
    #print(args)
    puzzle = parser.parser(args.files)
    t = Timer(lambda: run(puzzle, heuristic_fct(args)))
    print("exe time : {}".format(t.timeit(number=1)))
