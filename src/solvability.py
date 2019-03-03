import math

from src import Node
from src import config


def get_nb_of_inversion(node, verbose=False):
    inversion = 0
    for index, val in enumerate(node.grid):
        if val == 0:
            continue
        sub_grid = [value for i, value in enumerate(node.grid) if i > index]
        tmp = 0
        for sub_val in sub_grid:
            if sub_val == 0:
                continue
            if val > sub_val:
                inversion += 1
                tmp += 1
        if verbose:
            print("{} gives {} inversion".format(val, tmp))
    if verbose:
        print("total inversion = {}".format(inversion))
    return inversion


def is_solvable(node, verbose=False):
    if node.target is None:
        raise AttributeError("No target grid defined, can't check if solvable")
    solution_grid = Node.Node.dico2grid(node.target)
    solution_node = Node.Node(grid=solution_grid)
    node_inversion = get_nb_of_inversion(node)
    target_inversion = get_nb_of_inversion(solution_node)
    if config.TAQUIN_SIZE % 2 == 0:
        node_inversion += node.empty // config.TAQUIN_SIZE
        target_inversion += solution_node.empty // config.TAQUIN_SIZE
    if verbose:
        print("node inversion = {} ; target inversion = {}".format(node_inversion, target_inversion))
    return node_inversion % 2 == target_inversion % 2


def is_solvable_old(node):
    if node.target is None:
        raise AttributeError("No target grid defined, can't check if solvable")
    inversion = 0
    for index, val in enumerate(node.grid):
        if val == 0:
            continue
        x, y = node.target[val]
        target_index = Node.Node.xy_to_index(x, y)
        sub_grid = [value for i, value in enumerate(node.grid) if i > index]
        tmp = 0
        for sub_val in sub_grid:
            if sub_val == 0:
                continue
            x, y = node.target[sub_val]
            sub_target_index = Node.Node.xy_to_index(x, y)
            if target_index > sub_target_index:
                inversion += 1
                tmp += 1
        print("{} gives {} inversion".format(val, tmp))
    print("total inversion = {}".format(inversion))
    if config.TAQUIN_SIZE % 2 != 0:
        solvable = True if inversion % 2 == 0 else False
    elif (config.TAQUIN_SIZE - Node.Node.index_to_xy(node.empty)[0]) % 2 == 0:
        solvable = True if inversion % 2 != 0 else False
    else:
        solvable = True if inversion % 2 == 0 else False
    return solvable


if __name__ == "__main__":
    node = Node.Node(grid=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0])
    node = Node.Node(grid=[12, 1, 10, 2, 7, 11, 4, 14, 5, 0, 9, 15, 8, 13, 6, 3])
    config.TAQUIN_SIZE = int(math.sqrt(len(node.grid)))
    target = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (0, 3),
        5: (1, 0),
        6: (1, 1),
        7: (1, 2),
        8: (1, 3),
        9: (2, 0),
        10: (2, 1),
        11: (2, 2),
        12: (2, 3),
        13: (3, 0),
        14: (3, 1),
        15: (3, 2),
        0: (3, 3)
    }
    node.set_target_grid(target=target)
    solvable = is_solvable(node)
    print("solvable = {}".format(solvable))
