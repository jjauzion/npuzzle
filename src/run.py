from src import solvability
from src import PathFinder
from src import Node


def get_heuristic_fct_name(args):
    if args.uniform_cost:
        Node.Node.distance_between_node = 0
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


def run(grid, args=None, heuristic=None, verbose=False):
    if bool(args) == bool(heuristic):
        raise AttributeError("only one of args or heuristic shall be defined")
    elif args is not None:
        heuristic_fct = get_heuristic_fct_name(args)
    else:
        heuristic_fct = heuristic
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
