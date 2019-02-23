import unittest


from src import PathFinder
from src import Node


class TestValidPuzzle(unittest.TestCase):

    def setUp(self):
        self.path = PathFinder.PathFinder()

    def test_puzzle_1(self):
        start_node = Node.Node(grid=[8, 3, 4, 2, 1, 5, 7, 6, 0])
        self.path.set_start_node(start_node)
        self.path.a_star(verbose=1)
        self.assertEqual(self.path.solution["nb_move"], 8)
        self
