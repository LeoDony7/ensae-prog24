## Implementation of A* algorithm
import heapq
m=9
n=5

class Nodee():
    
    def __init__(self,liste,h=0,g=0):
        self.liste=liste
        self.h=h
        self.g=g
        self.f=self.h+self.g  # f =g+h avec g coût pour aller jusqu'au noeud et h distance estimée jusqu'à l'arrivée
                            ## attention f est ce qu'on appelle souvent heuristique
    def __lt__(self,noeud):
        return self.f<noeud.f
    
    

# S'il y a k cases non à leur place, il faut au minimum k//2 swaps pour arriver à la solution

def h(liste):
    node_final=tuple([i for i in range(1,n*m+1)]+[n]+[m])
    S=0
    for i in range(len(liste)):
        if liste[i]!=node_final[i]:
            S+=1
    return S//2


def A_starr(self,src,rch):
    open_list=[]
    heapq.heapify(open_list)
    closed_list={} # dictionnaire des Nodes deja parcourus, la clé sera un Node et la valeur associée sera Node.liste
    dict_chemin={}
    start_node=Nodee(src,0,0)
    open_list.append(start_node)
    dict_chemin[start_node]=[start_node] # dictionnaire qui à chaque Node N donne la liste de Node permettant d'arriver à N depuis src
    while len(open_list)!=0:
        u=heapq.heappop(open_list)  # u est un Node
        if u.liste==rch:
            return [noeud.liste for noeud in dict_chemin[u]]  # on ne veut que le chemin de listes (listes qui sont les noeuds du graphe)
        neighbours=self.graphe[u.value] # les éléments de neighbours sont des listes
        node_neighbours=[Nodee(i,h(i),u.g +1) for i in neighbours]
        for v in node_neighbours:  # v est un node
            Nodes_with_same_value=[]
            for k in open_list:
                if (k.liste==v.liste and k.f<v.f):
                    Nodes_with_same_value.append(k)
            # Ce sont les Node de open_list qui ont la même liste que le voisin mais avec une heuristique plus petite
            if (v not in closed_list) or Nodes_with_same_value==[]:
                open_list.append(v)
                dict_chemin[v]=dict_chemin[u]+[v]
        closed_list[u]=u.liste

