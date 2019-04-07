import argparse

from timeit import Timer
from src import parser
from src import error
from src import run


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    group = arg_parser.add_mutually_exclusive_group()
    group.add_argument('-M', '--Manhatan', action='store_true', help="(default heuristic)")
    group.add_argument('-H', '--Hamming_distance', action='store_true')
    group.add_argument('-L', '--Linear_conflict', action='store_true')
    group.add_argument('-E', '--Euclidian', action='store_true')
    group.add_argument('-G', '--greedy_search', action='store_true')
    arg_parser.add_argument('--old', action='store_true', help="run a start without heap push opti")
    arg_parser.add_argument('-U', '--uniform_cost', action='store_true')
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
        t = Timer(lambda: run.run(puzzle, args, args.verbose))
        print("exe time : {}".format(t.timeit(number=1)))
    else:
        run.run(puzzle, args, args.verbose)
