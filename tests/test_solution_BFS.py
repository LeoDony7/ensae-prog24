# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import Solver

class Test_IsSorted(unittest.TestCase):
    def test_grid_test(self):
        grid=Grid.grid_from_file("input/grid_test.in")
        grid_sol=Solver(grid)
        self.assertEqual(grid_sol.get_solution_bfs(),[((0, 0), (1, 0)), ((0, 1), (0, 2)), ((0, 0), (0, 1)), ((0, 2), (1, 2)), ((0, 1), (0, 2)), ((1, 1), (1, 2)), ((1, 0), (1, 1))])
       

if __name__ == '__main__':
    unittest.main()