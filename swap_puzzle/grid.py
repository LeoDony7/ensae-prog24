"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random


class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    coordinates: dict[int,(int,int)]
        Gives coordinates in the grid of each integer between 1 and m*n. coordinates[k] returns the coordinates (i_k,j_k) of the cell containing k
    key: tuple(int)
        An unique immutable key representing a grid. The k-th number in the tuple is the number in the k-th cell of the grid, cells being read line by line from left to right
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The initial state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state
        self.coordinates={self.state[i][j] :(i,j) for i in range(m) for j in range(n)}
        K=[]
        for ligne in self.state:
            for i in ligne:
                K.append(i)
        self.key=tuple(K)

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        for i in range(0, self.m -1):
            for j in range(0,self.n-1):
                if self.state[i][j]!=self.n*i+j+1:
                    return False
        return True

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        (i_1,j_1), (i_2,j_2)= cell1,cell2
        if (i_1==i_2 and abs(j_1 -j_2)<=1) or (j_1==j_2 and abs(i_1 -i_2)<=1):
            value_1=self.state[i_1][j_1]
            value_2=self.state[i_2][j_2]
            self.state[i_1][j_1]=value_2
            self.state[i_2][j_2]=value_1
            ##Updating coordinates of each integer
            self.coordinates={self.state[i][j] :(i,j) for i in range(self.m) for j in range(self.n)}
        else:
            raise ValueError

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for pair in cell_pair_list:
            (i_1,j_1), (i_2,j_2)= pair[0],pair[1]
            if (i_1==i_2 and abs(j_1 -j_2)<=1) or (j_1==j_2 and abs(i_1 -i_2)<=1):
                value_1=self.state[i_1][j_1]
                value_2=self.state[i_2][j_2]
                self.state[i_1][j_1]=value_2
                self.state[i_2][j_2]=value_1
                ##Updating coordinates of each integer
                self.coordinates={self.state[i][j] :(i,j) for i in range(self.m) for j in range(self.n)}
            else:
                raise ValueError
            
    def are_neighbours(self,grille):
        '''
        we assume that the 2 grids are same-sized
        '''
        differents_cells=[]
        for i in range(len(grille.key)):
            if grille.key[i]!=self.key[i]:
                differents_cells.append(self.coordinates[self.key[i]])
        if differents_cells==[]:
            return True            
        if len(differents_cells)==2:
            (i_1,j_1), (i_2,j_2)= differents_cells[0],differents_cells[1]
            if (i_1==i_2 and abs(j_1 -j_2)<=1) or (j_1==j_2 and abs(i_1 -i_2)<=1):
                return True
        return False
    ##transformer la fonction pour qu'elle s'utilise sur les tuples
    ##il s'agit surtout de retrouver la formule qui donne (i,j) à partir de k 
    ##voir si differents_cells peut être écrite en compréhension
    ##voir si on modifie la classe Solver pour que cette fonction en soit une méthode


    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid


