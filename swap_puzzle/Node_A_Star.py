'''
This is a module containing useful functions and class for the A* algorithm
'''

class Node():
    '''
    A class representing nodes for A*

    Attributes:
    -----------
    noeud : NodeType
        The node you want to represent, the node can be of any immutable type, e.g., integer, float, or string.
    f : int
        f is the sum of g and h
    g : int
        g is the cost to go to the node. Here it would be the number of node to go from the source node to the node
    h: int
        h is the estimated distance between the node and the destination node
    '''
    def __init__(self,noeud,h=0,g=0):
        '''
        Initializes the Node with a node and default values of g and h  

        Parameters: 
        -----------
        noeud: NodeType
            The node you want to represent
        h : int, optional
            the value of estimated distance
        g : int, optional
            the value of the cost
        '''
        self.noeud=noeud   
        self.h=h
        self.g=g
        self.f=self.h+self.g 

       
    def __lt__(self,other_Node):
        '''
        Overloading the "<" operator in order to compare 2 Nodes in a heapq.

        Arguments:
        ----------
        other_Node : Node
            An other Node to compare with
        
        Node A is lesser than Node B if and only if A.f < B.f
        '''
        return self.f<other_Node.f
    

def h(noeud):
    '''
    Function that calculate the estimated distance between a node and the destination node.
    Here the node is a grid key, as explained in grid.py
    And the destination node is the key of the sorted grid

    Parameters:
    -----------
    noeud : tuple
        A node, which is a grid key.
    '''
    node_final=tuple([i for i in range(1,noeud[-2]*noeud[-1]+1)]+[noeud[-2]]+[noeud[-1]])
    S=0
    for i in range(len(noeud)):
        if noeud[i]!=node_final[i]:
            S+=1
    return S//2
    