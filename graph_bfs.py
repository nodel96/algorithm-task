class Graph:
    """
    A Graph class that can represent either directed or undirected graphs.
    """
    
    def __init__(self, filename=None, directed=False, delimiter=None):
        """
        Initialize a Graph object. If a filename is specified, populate the Graph
        object by reading data from the specified file using the given delimiter.
        """
        self._directed = directed
        self._e = 0  # Number of edges
        self._adj = dict()  # Adjacency list representation
        
        if filename is not None:
            with open(filename, 'r') as f:
                lines = f.read().split('\n')
                for line in lines:
                    if line:  # Ensure the line is not empty
                        names = line.split(delimiter)
                        for i in range(1, len(names)):
                            self.addEdge(names[0], names[i])

    def addEdge(self, v, w):
        """
        Add an edge to the graph between vertex v and vertex w.
        """
        if not self.hasVertex(v):
            self._adj[v] = set()
        if not self.hasVertex(w):
            self._adj[w] = set()
        if not self.hasEdge(v, w):
            self._e += 
