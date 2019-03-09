import unittest
import pickle
from pathlib import Path


from src import PathFinder
from src import Node
from src import config


class TestValidPuzzle(unittest.TestCase):

    def setUp(self):
        self.pathfinder = PathFinder.PathFinder()

    def test_puzzle_1(self):
        config.TAQUIN_SIZE = 3
        start_node = Node.Node(grid=[8, 3, 4, 2, 1, 5, 7, 6, 0])
        with Path("unit_test/solution/{}.pkl".format(start_node.id)).open(mode='rb') as file:
            solution = pickle.load(file)
        self.pathfinder.set_start_node(start_node)
        self.pathfinder.a_star()
        self.assertEqual(self.pathfinder.solution["nb_move"], solution["nb_move"])

    def test_puzzle_2(self):
        config.TAQUIN_SIZE = 3
        start_node = Node.Node(grid=[4, 7, 6, 3, 0, 5, 1, 8, 2])
        with Path("unit_test/solution/{}.pkl".format(start_node.id)).open(mode='rb') as file:
            solution = pickle.load(file)
        self.pathfinder.set_start_node(start_node)
        self.pathfinder.a_star()
        self.assertEqual(self.pathfinder.solution["nb_move"], solution["nb_move"])

    def test_puzzle_3(self):
        config.TAQUIN_SIZE = 3
        start_node = Node.Node(grid=[1, 7, 0, 8, 5, 3, 6, 4, 2], heuristic_fct="linear_conflict")
        self.pathfinder.set_start_node(start_node)
        self.pathfinder.a_star()
        self.assertEqual(self.pathfinder.solution["nb_move"], 16)

    def test_puzzle_4(self):
        config.TAQUIN_SIZE = 4
        start_node = Node.Node(grid=[1, 14, 7, 6, 11, 12, 2, 8, 4, 0, 3, 5, 15, 10, 9, 13], heuristic_fct="linear_conflict")
        self.pathfinder.set_start_node(start_node)
        self.pathfinder.a_star()
        self.assertEqual(self.pathfinder.solution["nb_move"], 44)

    def test_puzzle_5(self):
        config.TAQUIN_SIZE = 4
        start_node = Node.Node(grid=[1, 10, 2, 3, 0, 12, 14, 8, 9, 13, 4, 6, 11, 15, 7, 5], heuristic_fct="linear_conflict")
        self.pathfinder.set_start_node(start_node)
        self.pathfinder.a_star()
        self.assertEqual(self.pathfinder.solution["nb_move"], 32)
