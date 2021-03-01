class Graph:

    def __init__(self, v):
        self.v = v
        self.adj = [[None]]*v

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def adj(self, v):
        return self.adj(v)
