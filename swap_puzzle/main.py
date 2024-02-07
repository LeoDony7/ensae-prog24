from grid import Grid
from solver import Solver
from solver import are_neighbours
from graph import Graph
from solver import what_is_the_swap

'''
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

gr2=Graph.graph_from_file("../input/graph2.in")

print(gr2)

for i in range(1,21):
    print(i)
    print(gr2.bfs(2,i))

print(g.key)
print(h.key)

import itertools

k=itertools.permutations([1,2,3,4])
for i in k:
    print (i)

essai=Solver(g)

essai.get_solution_bis()



g_simple_swap=Grid.grid_from_file("../input/grid0_simple_swap.in")
print(g_simple_swap)

g_double_swap=Grid.grid_from_file("../input/grid0_double_swap.in")

print(g_double_swap)
'''
'''
data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)
print(g.key.tuple)

g1=Grid.grid_from_file("../input/grid0_simple_swap.in")
print(g1)
print(g1.key.tuple)

g2=Grid.grid_from_file("../input/grid0_double_swap.in")
print(g2)
print(g2.key.tuple)

print(g.key.are_neighbours(g1.key))
print(g.key.are_neighbours(g2.key))
'''

'''
A=(2,4,3,1,2,2)
print(A)
B=(4,2,3,1,2,2)
C=(4,1,3,2,2,2)

print(are_neighbours(A,B))
print(are_neighbours(A,C))
print(are_neighbours(C,B))


data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)

Essai=Solver(g)

Essai.get_solution_bis()

h=Grid.grid_from_file("../input/grid2.in")
print(h)

essai2= Solver(h)

essai2.get_solution_bis()
'''

T= Grid.grid_from_file("../input/grid_test.in")
Test=Solver(T)
Test.get_solution_bis()


