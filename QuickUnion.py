
class QuickUnion:
    def __init__(self, n):
        self.id = []
        for i in range(n):
            self.id.append(i)

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        self.id[i] = j


if __name__ == '__main__':
    quickUnion = QuickUnion(10)
    quickUnion.union(5, 6)
    quickUnion.union(0, 2)
    quickUnion.union(0, 5)
    print(quickUnion.connected(2, 6))

