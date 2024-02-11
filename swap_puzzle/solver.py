from grid import Grid
from graph import Graph
import itertools

def are_neighbours(tuple1,tuple2):
    '''
    This function checks if 2 tuples are the key of 2 grids that are neighbours, i.e. we can find a swap to go from one to another
    It returns a boolean.

    Parameters:
    -----------
    tuple1:
        a tuple representing a n*m grid
    tuple2:
        another tuple representing a n*m grid (same size of tuple1)

    We assume that this function is always used on tuples representing a grid.
    
    If tuple1=tuple2, the function returns False.
    '''
    differents_cells=[]
    n=tuple1[-2]
    for i in range(len(tuple1)-2):
        if tuple2[i]!=tuple1[i]:
            differents_cells.append((i//n,i%n))    
    if len(differents_cells)==2:
        (i_1,j_1), (i_2,j_2)= differents_cells[0],differents_cells[1]
        if (i_1==i_2 and abs(j_1 -j_2)<=1) or (j_1==j_2 and abs(i_1 -i_2)<=1):
            return True
    return False


def what_is_the_swap(tuple1,tuple2):
    '''
    This function is only used on tuples that we already know they are neighbours.
    It return coordinates of the two cells of the swap between grids represented by these tuples.
    The format of the result is [(i1,j1),(i2,j2)].

    Parameters:
    -----------

    tuple1:
        a tuple representing a n*m grid
    tuple2:
        a tuple representing a n*m grid, this one being a neigbhour of the one represented by tuple1 
    '''
    differents_cells=[]
    n=tuple1[-2]
    for i in range(len(tuple1)-2):
        if tuple2[i]!=tuple1[i]:
            differents_cells.append((i//n,i%n))
    return differents_cells



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
        This one is the naive solution described in question 3

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
        This is the solution exposed in the question 7

        The principle of this solver is to create a graph where each node represents a state the grid can take,
        and to found the shortest path from the initial state to the solved state using a BFS algorithm.

        The format of the result is still [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].

        '''
        permutation=[i for i in range(1,(self.puzzle.n*self.puzzle.m)+1)]
        liste_permutation=itertools.permutations(permutation) #this list stocks all permutations of the grid as tuples
        my_graph=Graph([i+(self.puzzle.n,self.puzzle.m) for i in liste_permutation])
        #each node of the graph is the key of one of the grid state
        for node1 in my_graph.nodes:
            for node2 in my_graph.nodes:
                if are_neighbours(node1,node2):
                    if (node2 not in my_graph.graph[node1] or node1 not in my_graph.graph[node2]):
                        my_graph.add_edge(node1,node2)
        #for each pair of nodes in the graph, we add an edge to the graph if nodes are neighbours
        key_sorted=tuple(permutation+[self.puzzle.n]+[self.puzzle.m])
        #this one is the key corresponding the solved state of the grid
        node_path=my_graph.bfs(self.puzzle.key,key_sorted)
        if node_path==None:
            print("This grid cannot be solved")
        else:
            swap_list=[tuple(what_is_the_swap(node_path[i],node_path[i+1])) for i in range(0, len(node_path)-1)]
            #just rewriting the result to get the right format
            print(swap_list)

## The complexity of the creation of the graph is O((m*n)!)
## The complexity of the BFS algorithm is O((n*m)! + nb_edges)
## With such a complexity, this solver is great until for grid with approximately 6 or less cells.
## When n*m goes greater than 8 or 9, (n*m)! is too large and it tooks a while to solve the gid