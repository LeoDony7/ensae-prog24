from grid import Grid
from solver import Solver

g = Grid(2, 3)
print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)

h=Grid.grid_from_file("../input/grid4.in")
print(h)

essai2= Solver(h)

essai2.get_solution()


