from grid import Grid
from graph import Graph
import itertools

def are_neighbours(tuple1,tuple2):
    differents_cells=[]
    n=tuple1[-2]
    for i in range(len(tuple1)-2):
        if tuple2[i]!=tuple1[i]:
            differents_cells.append((i//n,i%n))
    if differents_cells==[]:
        return True            
    if len(differents_cells)==2:
        (i_1,j_1), (i_2,j_2)= differents_cells[0],differents_cells[1]
        if (i_1==i_2 and abs(j_1 -j_2)<=1) or (j_1==j_2 and abs(i_1 -i_2)<=1):
            return True
    return False



class Solver(): 
    """
    A solver class, it contains methods to resolve a swap puzzle problem.

    Attributes:
    -----------
    puzzle : grid
        The grid to be solved

    """
    def __init__(self,grille):
        '''
        Initializes the solver.

        Parameters:
        -----------

        grille : grid
            the grid to be solved
        '''    
        self.puzzle = grille
       
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 

        The principle of this resolution is to solve the puzzle by putting 1 on the right cell, then doing the same with 2, etc... until the puzzle is solved.
        First are done swaps that put the number on the right column and then those changing the line. By doing this way, placing correctly the k-th number doesn't change the position of previous number, that is already correct.
        """
        liste_swap=[]
        nombre_cases=self.puzzle.m*self.puzzle.n
        for k in range(1,nombre_cases+1):
            ##Coordinates of k just before starting putting it at the right place
            i_k,j_k = self.puzzle.coordinates[k] 
            ##Coordinates of the cell where k must be placed
            i0,j0= (k-1)//self.puzzle.n,(k-1)%self.puzzle.n 
            if j_k>j0:
                liste_cases= [(i_k,j_k)]+[(i_k,j) for j in range(j_k-1,j0-1,-1)]+[(i,j0) for i in range(i_k-1,i0-1,-1)]
            else :
                liste_cases= [(i_k,j_k)]+[(i_k,j) for j in range(j_k+1,j0+1)]+[(i,j0) for i in range(i_k-1,i0-1,-1)]
            liste_swap_k=[(liste_cases[i],liste_cases[i+1])for i in range(len(liste_cases)-1)]
            self.puzzle.swap_seq(liste_swap_k)
            liste_swap+=liste_swap_k
        print(liste_swap)

    def get_solution_bis(self):
        '''
        décrire la fonction
        '''
        permutation=[i for i in range(1,(self.puzzle.n*self.puzzle.m)+1)]
        liste_permutation=itertools.permutations(permutation)
        my_graph=Graph([i+(self.puzzle.n,self.puzzle.m) for i in liste_permutation])
        for node1 in my_graph.nodes:
            for node2 in my_graph.nodes:
                if are_neighbours(node1,node2):
                    if (node2 not in my_graph.graph[node1] or node1 not in my_graph.graph[node2]):
                        my_graph.add_edge(node1,node2)
        print(my_graph)

##l'arête avec soi-même se met 2 fois dans la liste d'adjacence