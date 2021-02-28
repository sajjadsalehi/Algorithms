class BinaryHeap:

    def __init__(self):
        self.items = []
        self.insert(None)

    def insert(self, key):
        self.items.append(key)
        self.swim(len(self.items)-1)

    def exchange(self, item1, item2):
        temp = self.items[item1]
        self.items[item1] = self.items[item2]
        self.items[item2] = temp

    def swim(self, key):
        while key > 1 and self.items[int(key/2)] < self.items[key]:
            self.exchange(key, int(key/2))
            key = int(key/2)

    def sink(self, k):
        while 2*k < len(self.items):
            j = 2*k
            if j < len(self.items) and self.items[j] < self.items[j+1]:
                j += 1
            if self.items[k] >= self.items[j]:
                break
            self.exchange(k, j)
            k = j

    def delMax(self):
        max = self.items[1]
        self.exchange(1, len(self.items)-1)
        self.sink(1)
        self.items.pop(-1)
        return max
