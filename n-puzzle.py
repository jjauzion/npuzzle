import argparse

from timeit import Timer
from src import Node
from src import PathFinder
from src import parser
from src import solvability
from src import error


def run(grid, heuristic_fct, verbose):
    start_node = Node.Node(grid=grid, heuristic_fct=heuristic_fct)
    solution = Node.Node.get_solution()
    start_node.set_target_grid(solution)
    print("Start node :")
    print(start_node)
    solvable = solvability.is_solvable(start_node)
    if not solvable:
        print("Puzzle is unsolvable")
        return
    else:
        print("Puzzle is solvable")
    algo = PathFinder.PathFinder(start_node=start_node)
    algo.a_star(verbose)
    algo.print_solution()


def heuristic_fct(args):
    if args.Linear_conflict:
        return "linear_conflict"
    elif args.Euclidian:
        return "euclidian"
    elif args.Hamming_distance:
        return "hamming_distance"
    elif args.greedy_search:
        return "greedy_search"
    elif args.uniform_cost:
        return "uniform_cost"
    else:
        return "manhanttan"


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    group = arg_parser.add_mutually_exclusive_group()
    group.add_argument('-M', '--Manhatan', action='store_true', help="(default heuristic)")
    group.add_argument('-H', '--Hamming_distance', action='store_true')
    group.add_argument('-L', '--Linear_conflict', action='store_true')
    group.add_argument('-E', '--Euclidian', action='store_true')
    group.add_argument('-G', '--greedy_search', action='store_true')
    group.add_argument('-U', '--uniform_cost', action='store_true')
    arg_parser.add_argument('-t', '--timer', action='store_true', help="print total execution time")
    arg_parser.add_argument('-v', '--verbose', action='store_true')
    arg_parser.add_argument("files", metavar="file", nargs="*", help="input file with a puzzle")
    args = arg_parser.parse_args()
    try:
        puzzle = parser.parser(args.files)
    except error.ParsingError as err:
        print("Parsing Error : {}".format(err.message))
        exit(1)
    if args.timer:
        t = Timer(lambda: run(puzzle, heuristic_fct(args), args.verbose))
        print("exe time : {}".format(t.timeit(number=1)))
    else:
        run(puzzle, heuristic_fct(args), args.verbose)
