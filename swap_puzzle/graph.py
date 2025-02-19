"""
This is the graph module. It contains a minimalistic Graph class.
"""
from Node_A_Star import Node
from Node_A_Star import h
import heapq

class Graph:
    """
    A class representing undirected graphs as adjacency lists. 

    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [neighbor1, neighbor2, ...]
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    edges: list[tuple[NodeType, NodeType]]
        The list of all edges
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 

        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes 
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
        self.edges = []
        
    def __str__(self):
        """
        Prints the graph as a list of neighbors for each node (one per line)
        """
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the graph with number of nodes and edges.
        """
        return f"<graph.Graph: nb_nodes={self.nb_nodes}, nb_edges={self.nb_edges}>"

    def add_edge(self, node1, node2):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 
        When adding an edge between two nodes, if one of the ones does not exist it is added to the list of nodes.

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        self.nb_edges += 1
        self.edges.append((node1, node2))

    def bfs(self, src, dst): 
        """
        Finds a shortest path from src to dst by BFS.  

        Parameters: 
        -----------
        src: NodeType
            The source node.
        dst: NodeType
            The destination node.

        Output: 
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """ 
        visited=[]
        queue=[src]
        path={i:[] for i in self.nodes}
        path[src]=[src]
        # path est le dictionnaire donnant le chemin jusqu'à un noeud
        # path[noeud]=[src,n1,n2,...,noeud] où les ni sont des noeuds
        while len(queue)>0:
            node=queue.pop(0)
            if node not in visited:
                visited.append(node)
                neighbours=self.graph[node]
                for neighbour in neighbours:
                    if neighbour not in queue:
                        path[neighbour]+=path[node]+[neighbour]
                    queue.append(neighbour)
            if node==dst:
                return path[node]
        return None   
    

    ## Aller voir le fichier Node_A_Star.py avant de lire la suite
    

    def bfs_upgrade(self, src, dst):
        """
        Finds a shortest path from src to dst by BFS.
        This version is upgraded. We use a priority queue instead of a normal queue when exploring a new node.  

        Parameters: 
        -----------
        src: NodeType
            The source node.
        dst: NodeType
            The destination node.

        Output: 
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """ 
        visited=[]
        # Les élements de visited sont des noeuds, les noeuds déja visité lors du parcours du graphe
        queue=[]
        heapq.heapify(queue)
        # queue est la file de priorité
        src_node=Node(src,0,0)
        # Les élements de queue sont des Nodes, comme défini dans le fichier Node_A_Star.py
        # On ne définit ici que l'heuristique h du noeud, qui est une estimation de la distance à l'arrivée. On ne s'intéresse pas au cout pour arriver au noeud.
        queue.append(src_node)
        path={}
        path[src]=[src]
        # path est le dictionnaire donnant le chemin jusqu'à un noeud
        # path[noeud]=[src,n1,n2,...,noeud] où les ni sont des noeuds
        while len(queue)>0:
            node=heapq.heappop(queue)
            # node est un Node
            if node.noeud not in visited:
                visited.append(node.noeud)
                neighbours=self.graph[node.noeud]
                # Liste des voisins du noeud exploré. Liste de noeuds
                neighbours_node=[Node(u,h(u),0) for u in neighbours]
                # Liste des voisins du noeud exploré, avec l'heuristique de chaque voisin. Liste de Nodes
                for neighbour in neighbours_node: 
                    if neighbour not in queue:
                        path[neighbour.noeud]=path[node.noeud]+[neighbour.noeud]
                    queue.append(neighbour)
            if node.noeud==dst:
                return path[node.noeud]
        return None  


    def A_star(self,src,dst):
        '''
        Finds a shortest path to src to dst by A*.

        Parameters:
        -----------
        src: NodeType
            The source node.
        dst: NodeType
            The destination node.
        
        Output: 
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src  
        '''
        ## Initialisation
        open_list=[]
        heapq.heapify(open_list)
        # open_list est la file de priorité, ses élements sont des Nodes, puisqu'on veut classer les élements selon la relation de comparaison sur la classe Node
        closed_list={}
        # closed _list est un dictionnaire qui stocke les noeuds déjà parcourus, les clés sont des Nodes, les valeurs sont des tuples. 
        # Si le noeud x a déjà été parcouru, closed_list[Node(x)]=Node(x).noeud
        dict_chemin={}
        # dict_chemin stocke le chemin jusqu'à chaque noeud depuis src, les clés sont des Nodes et les valeurs des listes de Nodes.
        # dict_chemin[Node(x)]=[start_node, ..., Node(x)]
        start_node=Node(src,0,0) 
        # start_node est le Node correspondant à src avec un coût et une estimation valant 0
        open_list.append(start_node)
        dict_chemin[start_node]=[start_node]

        ## Boucle
        while len(open_list)!=0:
            u=heapq.heappop(open_list)
            # u est un Node
            if u.noeud==dst:
                return [X.noeud for X in dict_chemin[u]] 
            # Puisqu'on veut retourner une liste de noeuds (qui sont des tuples), donc on ne récupère que les tuples correspondant à chaque Node dans le chemin 
            neighbours=self.graph[u.noeud]
            # neighbours est une liste contenant tout les noeuds voisins du noeud représenté par le Node u
            node_neighbours=[Node(i,h(i),u.g +1) for i in neighbours]
            # On transforme cette liste de noeuds en liste de Nodes en calculant le coût et l'estimation de chaque noeud
            for v in node_neighbours:
                # v est un Node
                Same_noeud=[]
                for k in open_list:
                    if (k.noeud==v.noeud and k.f<v.f):
                        Same_noeud.append(k)
                # Ce sont les Node de open_list qui représentent le même noeud que v mais avec une heuristique plus petite
                if (v not in closed_list) or Same_noeud==[]:
                    # On vérifie les 2 conditions nécéssaires pour pouvoir ajouter le voisin dans l'open_list
                    # Ces 2 conditions sont : v n'est pas déjà dans la closed_list, v n'est pas dans l'open_list avec une heuristique plus faible
                    open_list.append(v)
                    dict_chemin[v]=dict_chemin[u]+[v]
                    # On met à jour le chemin jusqu'aux voisins ajoutés                
            closed_list[u]=u.noeud
            # On ajoute le noeud visité à la closed_list
        return None

    @classmethod
    def graph_from_file(cls, file_name):
        """
        Reads a text file and returns the graph as an object of the Graph class.

        The file should have the following format: 
            The first line of the file is 'n m'
            The next m lines have 'node1 node2'
        The nodes (node1, node2) should be named 1..n

        Parameters: 
        -----------
        file_name: str
            The name of the file

        Outputs: 
        -----------
        graph: Graph
            An object of the class Graph with the graph from file_name.
        """
        with open(file_name, "r") as file:
            n, m = map(int, file.readline().split())
            graph = Graph(range(1, n+1))
            for _ in range(m):
                edge = list(map(int, file.readline().split()))
                if len(edge) == 2:
                    node1, node2 = edge
                    graph.add_edge(node1, node2) # will add dist=1 by default
                else:
                    raise Exception("Format incorrect")
        return graph

