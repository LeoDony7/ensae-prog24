##On se sert plus de ce fichier normalement


class Key(str):

    '''
    def __init__(self,tuple):
        self.tuple=tuple
    '''

    def __init__(self):
        super().__init__()

    '''
    def are_neighbours(self,cle):
        differents_cells=[]
        n=self.tuple[-2]
        for i in range(len(cle.tuple)-2):
            if cle.tuple[i]!=self.tuple[i]:
                differents_cells.append((i//n,i%n))
        if differents_cells==[]:
            return True            
        if len(differents_cells)==2:
            (i_1,j_1), (i_2,j_2)= differents_cells[0],differents_cells[1]
            if (i_1==i_2 and abs(j_1 -j_2)<=1) or (j_1==j_2 and abs(i_1 -i_2)<=1):
                return True
        return False
    '''

    def are_neighbours(self,cle):
        differents_cells=[]
        n=self[-2]
        for i in range(len(cle)-2):
            if cle[i]!=self[i]:
                differents_cells.append((i//n,i%n))
        if differents_cells==[]:
            return True            
        if len(differents_cells)==2:
            (i_1,j_1), (i_2,j_2)= differents_cells[0],differents_cells[1]
            if (i_1==i_2 and abs(j_1 -j_2)<=1) or (j_1==j_2 and abs(i_1 -i_2)<=1):
                return True
        return False

