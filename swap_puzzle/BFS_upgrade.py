from Node_A_Star import Node
from Node_A_Star import h
import heapq



def bfs_upgrade(self, src, dst): 
    visited=[]
    # Dans visited les éléments sont des noeuds
    queue=[]
    heapq.heapify(queue)
    src_node=Node(src,0,0)
    # On réutilise la structure de Node utilisée pour A* mais ici on associe seulement une heuristique à un noeud, on ne définit pas le cout
    queue.append(src_node)
    # Dans queue les éléments sont des Nodes
    path={}
    path[src]=[src]
    # Dans path les clés sont des noeuds et les valeurs des listes de noeuds
    while len(queue)>0:
        node=heapq.heappop(queue) # node est un Node
        if node.noeud not in visited:
            visited.append(node.noeud)
            neighbours=self.graph[node.noeud] # voisins en tant que noeuds du graphe
            neighbours_node=[Node(u,h(u),0) for u in neighbours] # voisins en tant que Node
            for neighbour in neighbours_node: # on regarde les Nodes voisins
                if neighbour not in queue:
                    path[neighbour.noeud]=path[node.noeud]+[neighbour.noeud]
                queue.append(neighbour)
        if node.noeud==dst:
            return path[node.noeud]
    return None  
