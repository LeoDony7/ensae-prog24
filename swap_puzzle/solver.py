from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def __init__(self,grille):
    ## faire la description de cette fonction    
        self.probleme = grille
        self.solution = grille
       
        

    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        nombre_cases=self.probleme.m*self.probleme.n
        
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        raise NotImplementedError

