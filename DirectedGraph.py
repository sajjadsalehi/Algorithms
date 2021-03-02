class DirectedGraph:

    def __init__(self, v):
        self.v = v
        self.adj = [[None]]*v

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def adj(self, v):
        return self.adj(v)

    def size(self):
        return len(self.v)
