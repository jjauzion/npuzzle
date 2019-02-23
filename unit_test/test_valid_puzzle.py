import unittest
import pickle
from pathlib import Path


from src import PathFinder
from src import Node
from src import config


class TestValidPuzzle(unittest.TestCase):

    def setUp(self):
        self.path = PathFinder.PathFinder()

    def test_puzzle_1(self):
        config.TAQUIN_SIZE = 3
        start_node = Node.Node(grid=[8, 3, 4, 2, 1, 5, 7, 6, 0])
        with Path("unit_test/solution/{}.pkl".format(start_node.id)).open(mode='rb') as file:
            solution = pickle.load(file)
        self.path.set_start_node(start_node)
        self.path.a_star()
        self.assertEqual(self.path.solution["nb_move"], solution["nb_move"])

    def test_puzzle_2(self):
        config.TAQUIN_SIZE = 3
        start_node = Node.Node(grid=[8, 3, 4, 2, 1, 5, 7, 6, 0])
        with Path("unit_test/solution/{}.pkl".format(start_node.id)).open(mode='rb') as file:
            solution = pickle.load(file)
        self.path.set_start_node(start_node)
        self.path.a_star()
        self.assertEqual(self.path.solution["nb_move"], solution["nb_move"])
