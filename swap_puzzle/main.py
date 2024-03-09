from grid import Grid
from solver import Solver
from graph import Graph

'''
g = Grid(2, 3)
print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)


T= Grid.grid_from_file("../input/grid_test.in")
Test=Solver(T)
Test.get_solution()
Test.get_solution_bfs()



H=Grid.grid_from_file("../input/grid4.in")
H.representation_graphique()
'''

my_graph=Graph.graph_from_file("../input/graph2.in")

print(my_graph.bfs(4,10))

