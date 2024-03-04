"""
This is the graph module. It contains a minimalistic Graph class.
"""
from node import Node
from node import h
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
        #path=[[] for i in range(self.nb_nodes)]
        path_bis={i:[] for i in self.nodes}
        #path[src-1]=[src]
        path_bis[src]=[src]
        while len(queue)>0:
            node=queue.pop(0)
            if node not in visited:
                visited.append(node)
                neighbours=self.graph[node]
                for neighbour in neighbours:
                    if neighbour not in queue:  ##verifier ca pour être sur qu'on a pas de répétition de noeuds
                        #path[neighbour-1]+=(path[node-1]+[neighbour])
                        path_bis[neighbour]+=path_bis[node]+[neighbour]
                    queue.append(neighbour)
            if node==dst:
                #return path[node-1]
                return path_bis[node]
        return None   
    
    def A_star(self,src,rch):
        open_list=[]
        heapq.heapify(open_list)
        closed_list={} # dictionnaire des Nodes deja parcourus, la clé sera un Node et la valeur associée sera Node.liste
        dict_chemin={}
        start_node=Node(src,0,0)
        open_list.append(start_node)
        dict_chemin[start_node]=[start_node] # dictionnaire qui à chaque Node N donne la liste de Node permettant d'arriver à N depuis src
        while len(open_list)!=0:
            u=heapq.heappop(open_list)  # u est un Node
            if u.liste==rch:
                return [noeud.liste for noeud in dict_chemin[u]]  # on ne veut que le chemin de listes (listes qui sont les noeuds du graphe)
            neighbours=self.graph[u.liste] # les éléments de neighbours sont des listes
            node_neighbours=[Node(i,h(i),u.g +1) for i in neighbours]
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

