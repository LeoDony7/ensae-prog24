'''
This is the node module.
It contains a representation of nodes used in A* algorithm and a pseudo-distance used in A* algorithm
'''

class Node():
    
    def __init__(self,liste,h=0,g=0):
        self.liste=liste
        self.h=h
        self.g=g
        self.f=self.h+self.g  # f =g+h avec g coût pour aller jusqu'au noeud et h distance estimée jusqu'à l'arrivée
                            ## attention f est ce qu'on appelle souvent heuristique
    def __lt__(self,noeud):
        return self.f<noeud.f
    

def h(liste):
    node_final=tuple([i for i in range(1,liste[-2]*liste[-1]+1)]+[liste[-2]]+[liste[-1]])
    S=0
    for i in range(len(liste)):
        if liste[i]!=node_final[i]:
            S+=1
    return S//2
    