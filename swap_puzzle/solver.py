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
        For a given number, first are done swaps that put the number on the right column and then those changing the line. By doing this way, placing correctly the k-th number doesn't change the position of previous numbers, that are already corrects.
        """
        liste_swap=[]
        nombre_cases=self.puzzle.m*self.puzzle.n
        for k in range(1,nombre_cases+1):
            i_k,j_k = self.puzzle.coordinates[k]
            ## Coordonnées de k avant qu'on le déplace.
            i0,j0= (k-1)//self.puzzle.n,(k-1)%self.puzzle.n 
            ## Coordonnées de la case où doit être placé k.
            if j_k>j0:
                liste_cases= [(i_k,j_k)]+[(i_k,j) for j in range(j_k-1,j0-1,-1)]+[(i,j0) for i in range(i_k-1,i0-1,-1)]
            else :
                liste_cases= [(i_k,j_k)]+[(i_k,j) for j in range(j_k+1,j0+1)]+[(i,j0) for i in range(i_k-1,i0-1,-1)]
            # les cases par où doit passer k pour arriver à sa place dépend de si k est au départ dans
            # une colonne à gauche ou a droite de la colonne où il doit être placé.
            liste_swap_k=[(liste_cases[i],liste_cases[i+1])for i in range(len(liste_cases)-1)]
            self.puzzle.swap_seq(liste_swap_k)
            liste_swap+=liste_swap_k
        return liste_swap


    def get_solution_bfs(self):
        '''
        This is the solution exposed in the question 7

        The principle of this solver is to create a graph where each node represents a state the grid can take,
        and to found the shortest path from the initial state to the solved state using a BFS algorithm.

        The format of the result is still [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].

        '''
        permutation=[i for i in range(1,(self.puzzle.n*self.puzzle.m)+1)]
        liste_permutation=itertools.permutations(permutation) 
        # On crée toutes les permutations de [1,...,m*n] sous forme de tuples.
        my_graph=Graph([i+(self.puzzle.n,self.puzzle.m) for i in liste_permutation])
        # Chaque noeud du graphe est la clé d'un état de la grille.
        for node1 in my_graph.nodes:
            for node2 in my_graph.nodes:
                if are_neighbours(node1,node2):
                    if (node2 not in my_graph.graph[node1] or node1 not in my_graph.graph[node2]):
                        my_graph.add_edge(node1,node2)
        # Pour chaque paire de noeuds dans le graphe, on vérifie s'ils sont voisins et donc s'il faut ajouter une arête entre les 2.
        key_sorted=tuple(permutation+[self.puzzle.n]+[self.puzzle.m])
        # On explicite la clé correspondant à l'état trié de la grille, elle servira de destination dans le parcours de graphe.
        node_path=my_graph.bfs(self.puzzle.key,key_sorted)
        if node_path==None:
            return "This grid cannot be solved"
        else:
            swap_list=[tuple(what_is_the_swap(node_path[i],node_path[i+1])) for i in range(0, len(node_path)-1)]
            # node_path est une liste de noeuds donc on met le résultat au bon format, i.e. une liste de swaps (couple de cases)
            self.puzzle.swap_seq(swap_list)
            return swap_list

            

    def get_solution_A_star(self):
        '''
        This is the solution the improve of the question 7 solution, with A* instead of BFS.

        It doesn't need any further comments, because it is the same code as for get_solution_bfs.
        We just replaced BFS by A* in the search of a path between 2 nodes. 

        The format of the result is still [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].

        '''
        permutation=[i for i in range(1,(self.puzzle.n*self.puzzle.m)+1)]
        liste_permutation=itertools.permutations(permutation)
        my_graph=Graph([i+(self.puzzle.n,self.puzzle.m) for i in liste_permutation])
        for node1 in my_graph.nodes:
            for node2 in my_graph.nodes:
                if are_neighbours(node1,node2):
                    if (node2 not in my_graph.graph[node1] or node1 not in my_graph.graph[node2]):
                        my_graph.add_edge(node1,node2)
        key_sorted=tuple(permutation+[self.puzzle.n]+[self.puzzle.m])
        node_path=my_graph.A_star(self.puzzle.key,key_sorted)
        # La seule différence avec la solution précédente est qu'on utilise l'algorithme A* à la place de BFS
        if node_path==None:
            return "This grid cannot be solved"
        else:
            swap_list=[tuple(what_is_the_swap(node_path[i],node_path[i+1])) for i in range(0, len(node_path)-1)]
            self.puzzle.swap_seq(swap_list)
            return swap_list