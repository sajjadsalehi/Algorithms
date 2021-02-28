class PriorityQueue:

    def __init__(self):
        self.items = []

    def insert(self, key):
        self.items.append(key)

    def isEmpty(self):
        return len(self.items) == 0

    def delMax(self):
        return self.items.pop(self.items.index(max(self.items)))
