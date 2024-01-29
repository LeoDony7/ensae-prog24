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
        liste_swap=[]
        nombre_cases=self.probleme.m*self.probleme.n
        for k in range(1,nombre_cases+1):
            i_k,j_k = self.solution.coordinates[k] ##Coordonnées de k avant qu'il soit déplacé
            i0,j0= (k-1)//self.probleme.n,(k-1)%self.probleme.n ##Coordonnées de la case où doit être k
            if j_k>j0:
                liste_cases= [(i_k,j_k)]+[(i_k,j) for j in range(j_k-1,j0-1,-1)]+[(i,j0) for i in range(i_k-1,i0-1,-1)]
            else :
                liste_cases= [(i_k,j_k)]+[(i_k,j) for j in range(j_k+1,j0+1)]+[(i,j0) for i in range(i_k-1,i0-1,-1)]
            liste_swap_k=[(liste_cases[i],liste_cases[i+1])for i in range(len(liste_cases)-1)]
            self.solution.swap_seq(liste_swap_k)
            liste_swap+=liste_swap_k
        print(self.solution)
        print(liste_swap)

