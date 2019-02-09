import numpy as np

from . import Taquin
from . import config


def get_solution(taquin):
    """
    Retturn the solution to the taquin both as a Taquin object and as a dictionary
    :return: solution_as_a_taquin, solution_as_a_dictionary
    """
    solution = np.zeros((config.TAQUIN_SIZE, config.TAQUIN_SIZE), dtype=np.uint16)
    sol_dict = {}
    y = 0
    ymin = 0
    ymax = config.TAQUIN_SIZE - 1
    x= 0
    xmin = 0
    xmax = config.TAQUIN_SIZE - 1
    cpt = 1
    dir = 1
    for i in range(config.TAQUIN_SIZE * config.TAQUIN_SIZE):
        solution[x][y] = cpt
        sol_dict[cpt] = (x, y)
        cpt = cpt + 1 if cpt < config.TAQUIN_SIZE * config.TAQUIN_SIZE - 1 else 0
        if x == xmin and y < ymax:
            if dir == 4:
                ymin += 1
                dir = 1
            y += 1
        elif y == ymax and x < xmax:
            if dir == 1:
                xmin += 1
                dir = 2
            x += 1
        elif x == xmax and y > ymin:
            if dir == 2:
                ymax -= 1
                dir = 3
            y -= 1
        elif y == ymin and x > xmin:
            if dir == 3:
                dir = 4
                xmax -= 1
            x -= 1
    return solution, sol_dict


def taquin_to_dictionary(taquin):
    """
    Return the tacquin as a dictionary
    :return:
    """
    dictionary = {}
    iterator = np.nditer(taquin.grid, flags=['multi_index'])
    while not iterator.finished:
        dictionary[int(iterator[0])] = (iterator.multi_index[0], iterator.multi_index[1])
        iterator.iternext()
    return dictionary


def get_moved_taquin(taquin, move):
    """
    Create a new taquin, matching the taquin in argument after the required move
    :param move: Desired move. Choices : config.MOVE_[TOP|BOTTOM|LEFT|RIGHT]
    :return: New allocated taquin after the move if the move is possible ; None if the move is not possible
    """
    move_vect = [0, 0]
    move_vect[0] = -1 if move == config.MOVE_TOP else 1 if move == config.MOVE_BOTTOM else 0
    move_vect[1] = -1 if move == config.MOVE_LEFT else 1 if move == config.MOVE_RIGHT else 0
    if taquin.empty[0] + move_vect[0] < 0 or taquin.empty[0] + move_vect[0] >= config.TAQUIN_SIZE:
        return None
    if taquin.empty[1] + move_vect[1] < 0 or taquin.empty[1] + move_vect[1] >= config.TAQUIN_SIZE:
        return None
    new_taquin = Taquin.Taquin(grid=np.copy(taquin.grid))
    new_empty_coord = new_taquin.empty[0] + move_vect[0], new_taquin.empty[1] + move_vect[1]
    new_taquin.grid[new_empty_coord[0]][new_empty_coord[1]], new_taquin.grid[taquin.empty[0]][taquin.empty[1]] = \
        0, new_taquin.grid[new_empty_coord[0]][new_empty_coord[1]]
    new_taquin.empty = new_empty_coord
    return new_taquin


def generate_random_taquin():
    """
    Generate a new Taquin with a random grid.
    :param size: Size of the Taquin (i.e. taquin will be a grid of size * size)
    :return: new Taquin object
    """
    grid = np.arange(config.TAQUIN_SIZE * config.TAQUIN_SIZE)
    np.random.shuffle(grid)
    grid = grid.reshape((config.TAQUIN_SIZE, config.TAQUIN_SIZE))
    taquin = Taquin.Taquin(grid=grid)
    return taquin
