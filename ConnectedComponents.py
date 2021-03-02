from Graph import *


class ConnectedComponents:

    def __init__(self, graph):
        self.marked = [False]*graph.size()
        self.id = [0]*graph.size()
        self.count = 0

        for v in range(graph.size()):
            if not self.marked[v]:
                self.dfs(graph, v)
                self.count += 1

    def count(self):
        return self.count

    def id(self, v):
        return id[v]

    def dfs(self, graph, v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in graph.adj(v):
            if not self.marked[v]:
                self.dfs(graph, w)
