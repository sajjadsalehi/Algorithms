class TopologicalOrder:

    def __init__(self, graph, start):
        self.marked = []
        self.s = start
        self.reversePost = []
        self.dfs(graph, start)
        self.reverse()

    def dfs(self, graph, v):
        self.marked[v] = True
        for w in graph.adj(v):
            if not self.marked[w]:
                self.dfs(graph, w)
        self.reversePost.append(v)

    def reverse(self):
        self.reversePost.reverse()
