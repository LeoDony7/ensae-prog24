from grid import Grid

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

