class Graph:
    """
    Class for representing a graph, capable of reading data from a file to create the graph.
    Supports both directed and undirected graphs.
    """
    def __init__(self, filename=None, directed=False, delimiter=None):
        self._directed = directed
        self._e = 0
        self._adj = {}
        if filename:
            with open(filename, 'r') as f:
                for line in f:
                    parts = line.split(delimiter)
                    if len(parts) != 3:
                        continue
                    for i in range(1, len(parts), 2):
                        self.addEdge(parts[0], parts[i], float(parts[i+1]))

    def addEdge(self, v, w, weight):
        if not self.hasVertex(v):
            self._adj[v] = set()
        if not self.hasVertex(w):
            self._adj[w] = set()
        if not self.hasEdge(v, w, weight):
            self._e += 1
            self._adj[v].add((w, weight))
            if not self._directed:
                self._adj[w].add((v, weight))

    def adjacentTo(self, v):
        return iter(self._adj[v])

    def vertices(self):
        return iter(self._adj)

    def hasVertex(self, v):
        return v in self._adj

    def hasEdge(self, v, w, weight):
        return (w, weight) in self._adj[v]

    def countV(self):
        return len(self._adj)

    def countE(self):
        return self._e

    def degree(self, v):
        return len(self._adj[v])

    def __str__(self):
        return '\n'.join(f'{v}  {" ".join(f"{w} {weight}" for w, weight in neighbors)}' 
                         for v, neighbors in self._adj.items())


class PriorityQ:
    """
    Priority Queue implementation using a heap for efficient retrieval of the lowest priority item.
    """
    def __init__(self):
        self._pq = []
        self._entry_finder = {}
        self._REMOVED = '<removed-task>'
        self._counter = itertools.count()

    def isEmpty(self):
        return not self._entry_finder

    def insert(self, obj, priority):
        if obj in self._entry_finder:
            self.remove(obj)
        count = next(self._counter)
        entry = [priority, count, obj]
        self._entry_finder[obj] = entry
        heapq.heappush(self._pq, entry)

    def remove(self, obj):
        entry = self._entry_finder.pop(obj)
        entry[-1] = self._REMOVED

    def pop(self):
        while self._pq:
            priority, count, obj = heapq.heappop(self._pq)
            if obj is not self._REMOVED:
                del self._entry_finder[obj]
                return obj
        raise KeyError('pop from an empty priority queue')

    def __str__(self):
        return str(self._pq)


def d_shortest_paths(g, s):
    INFINITY = 1000000.0
    visited = set()
    distTo = {v: INFINITY for v in g.vertices()}
    parent = {v: 'default' for v in g.vertices()}
    parent[s] = -1
    distTo[s] = 0

    pq = PriorityQ()
    for v in g.vertices():
        pq.insert(v, distTo[v])

    while not pq.isEmpty():
        v = pq.pop()
        visited.add(v)
        for w, weight in g.adjacentTo(v):
            if w not in visited and distTo[w] > distTo[v] + weight:
                pq.remove(w)
                distTo[w] = distTo[v] + weight
                parent[w] = v
                pq.insert(w, distTo[w])

    return distTo, parent


def printPath(graph, city1, city2):
    distance, parent = d_shortest_paths(graph, city1)
    if distance[city2] == 1000000.0:
        print("This Path doesn't exist")
        return

    print(distance[city2])
    stack = []
    current = city2
    while current != -1:
        stack.append(current)
        current = parent[current]

    while stack:
        print(stack.pop())


# Example usage
G = Graph(filename='sweden.txt')
printPath(G, 'Kopparberg', 'Enbacka')
