# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import are_neighbours

class Test_IsSorted(unittest.TestCase):
    def test_grid1(self):
        grid0=Grid.grid_from_file("input/grid0.in")
        grid1=Grid.grid_from_file("input/grid0_simple_swap.in")
        grid2=Grid.grid_from_file("input/grid0_double_swap.in")
        self.assertEqual(are_neighbours(grid0.key,grid1.key),True)
        self.assertEqual(are_neighbours(grid0.key,grid2.key),False)

if __name__ == '__main__':
    unittest.main()