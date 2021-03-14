class DirectedGraph:

    def __init__(self, v):
        self.v = v
        self.adj = [[None]]*v

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def adj(self, v):
        return self.adj[v]

    def size(self):
        return len(self.v)

    def reverse(self):
        new_adjs = [[None]]*self.v
        for i in range(len(self.adj)):
            for j in range(len(self.adj[i])):
                new_adjs[j].append(i)
        self.adj = new_adjs
