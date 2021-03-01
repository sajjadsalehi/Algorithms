from Graph import *

class DepthFirstSearch:

    def __init__(self, graph, start):
        self.marked = []
        self.edgeTo = []
        self.s = start
        self.dfs(graph, start)

    def dfs(self, graph, v):
        self.marked[v] = True
        for w in graph.adj(v):
            if not self.marked[w]:
                self.dfs(graph, w)
                self.edgeTo[w] = v
