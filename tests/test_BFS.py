# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph

class Test_IsSorted(unittest.TestCase):
    def test_graph1(self):
        graph=Graph.graph_from_file("input/graph1.in")
        self.assertEqual(graph.bfs(1,7),[1,15,12,7])
    def test_graph2(self):
        graph=Graph.graph_from_file("input/graph2.in")
        self.assertEqual(graph.bfs(4,10),[4,18,17,10])
        self.assertEqual(graph.bfs(3,8),None)

if __name__ == '__main__':
    unittest.main()
