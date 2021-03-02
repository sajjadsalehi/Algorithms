class BreadthFirstSearch:

    def __init__(self, graph, start):
        self.marked = []
        self.edgeTo = []
        self.bfs(graph, start)

    def bfs(self, graph, start):
        queue = [start]
        self.marked[start] = True
        while len(queue) > 0:
            v = queue.pop(0)
            for w in graph.adj(v):
                if not self.marked[w]:
                    queue.append(w)
                    self.marked[w] = True
                    self.edgeTo[w] = v
