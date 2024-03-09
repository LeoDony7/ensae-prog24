## Imports

from grid import Grid
from solver import Solver
from graph import Graph



##

g = Grid(2, 3)
print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)


## Question n°3 

g = Grid.grid_from_file("../input/grid_test.in")

puzzle=Solver(g)

print(g)

print(puzzle.get_solution())


## Question n°4

g.representation_graphique()


## Question n°6

print(g.key)


## Question n°7

print(puzzle.get_solution_bfs())


## A*

print(puzzle.get_solution_A_star())



