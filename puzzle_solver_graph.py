class Graph:
    def __init__(self, filename=None, directed=False, delimiter=None):
        self._directed = directed
        self._e = 0
        self._adj = dict()
        if filename:
            with open(filename, 'r') as f:
                lines = f.read().split('\n')
                for line in lines:
                    names = line.split(delimiter)
                    for name in names[1:]:
                        self.addEdge(names[0], name)

    def addEdge(self, v, w):
        if not self.hasVertex(v):
            self._adj[v] = set()
        if not self.hasVertex(w):
            self._adj[w] = set()
        if not self.hasEdge(v, w):
            self._e += 1
            self._adj[v].add(w)
            if not self._directed:
                self._adj[w].add(v)

    def adjacentTo(self, v):
        return iter(self._adj[v])

    def vertices(self):
        return iter(self._adj.keys())

    def hasVertex(self, v):
        return v in self._adj

    def hasEdge(self, v, w):
        return w in self._adj[v]

    def countV(self):
        return len(self._adj)

    def countE(self):
        return self._e

    def degree(self, v):
        return len(self._adj[v])

    def __str__(self):
        return '\n'.join([f"{v}  {' '.join(w for w in self.adjacentTo(v))}" for v in self.vertices()])


class Queue:
    def __init__(self):
        self._first = None
        self._last = None
        self._length = 0

    def isEmpty(self):
        return self._first is None

    def enqueue(self, item):
        oldLast = self._last
        self._last = _Node(item, None)
        if self.isEmpty():
            self._first = self._last
        else:
            oldLast.next = self._last
        self._length += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        item = self._first.item
        self._first = self._first.next
        if self.isEmpty():
            self._last = None
        self._length -= 1
        return item

    def __len__(self):
        return self._length

    def __str__(self):
        items = []
        current = self._first
        while current:
            items.append(str(current.item))
            current = current.next
        return ' '.join(items)


class _Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


def legalMoves(N, string1):
    moves = []
    _index = string1.find('_')
    l = list(string1)

    if _index + 1 != (N + 1) * N - 1:
        if l[_index + 1] != '/':
            l[_index], l[_index + 1] = l[_index + 1], '_'
            moves.append(''.join(l))

    if _index != 0:
        if l[_index - 1] != '/':
            l[_index], l[_index - 1] = l[_index - 1], '_'
            moves.append(''.join(l))

    if _index + N + 1 <= (N + 1) * N - 1:
        l[_index], l[_index + N + 1] = l[_index + N + 1], '_'
        moves.append(''.join(l))

    if _index - N - 1 >= 0:
        l[_index], l[_index - N - 1] = l[_index - N - 1], '_'
        moves.append(''.join(l))

    return moves


def f(N, s):
    goal = ''.join([chr(ord('A') + i * N + j) for i in range(N) for j in range(N)] + ['/'] * N)[:-2] + '_'

    G = Graph(directed=True)
    Q = Queue()
    Q.enqueue(s)
    explored = {s}

    while Q._first:
        if Q._first.item == goal:
            break
        for i in legalMoves(N, Q._first.item):
            if i not in explored:
                G.addEdge(i, Q._first.item)
                Q.enqueue(i)
                explored.add(i)
        Q.dequeue()

    if not Q._first:
        print('No Solution')
        return

    stack = []
    temp = Q._first.item
    while temp != s:
        stack.append(temp)
        temp = lastState(G, temp)
    while stack:
        print(stack.pop())


def lastState(graph, string):
    return next(graph.adjacentTo(string), None)


# Example usage
# f(2, 'BC/A_')
