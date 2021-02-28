class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.count = 1


class Bst:

    def __init__(self):
        self.root = None

    def get(self, key):
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.val
        return None

    def put(self, key, value):
        self.root = self.putIt(self.root, key, value)

    def putIt(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self.putIt(node.left, key, value)
        elif key > node.key:
            node.right = self.putIt(node.right, key, value)
        else:
            node.value = value
        node.count = 1 + self.sizeIt(node.left) + self.sizeIt(node.right)
        return node

    def min(self):
        node = self.root
        minimum = None
        while node is not None:
            minimum = node.value
            node = node.left
        return minimum

    def minNode(self, node):
        minimum = None
        while node is not None:
            minimum = node
            node = node.left
        return minimum

    def max(self):
        node = self.root
        maximum = None
        while node is not None:
            maximum = node.value
            node = node.right
        return maximum

    def floor(self, key):
        node = self.floorIt(self.root, key)
        if node is None:
            return None
        return node.key

    def floorIt(self, node, key):
        if node is None:
            return None
        if key == node.value:
            return node
        if key < node.value:
            return self.floorIt(node.left, key)
        t = self.floorIt(node.right, key)
        if t is not None:
            return t
        else:
            return node

    def size(self):
        return self.sizeIt(self.root)

    def sizeIt(self, node):
        if node is None:
            return 0
        return node.count

    def rank(self, key):
        return self.rankIt(key, self.root)

    def rankIt(self, key, node):
        if node is None:
            return 0
        if key < node.key:
            return self.rankIt(key, node.left)
        if key > node.key:
            return 1 + self.sizeIt(node.left) + self.rankIt(key, node.right)
        else:
            return self.sizeIt(node.left)

    def keys(self):
        queue = []
        self.inOrder(self.root, queue)
        return queue

    def inOrder(self, node, queue):
        if node is None:
            return
        self.inOrder(node.left, queue)
        queue.append(node.value)
        self.inOrder(node.right, queue)

    def deleteMin(self):
        self.root = self.deleteMinByNode(self.root)

    def deleteMinByNode(self, node):
        if node.left is None:
            return node.right
        node.left = self.deleteMinByNode(node.left)
        node.count = 1 + self.sizeIt(node.left) + self.sizeIt(node.right)
        return node

    def delete(self, key):
        root = self.deleteByNode(self.root, key)

    def deleteByNode(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.deleteByNode(node.left, key)
        elif key > node.key:
            node.right = self.deleteByNode(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            t = node
            node = self.minNode(t.right)
            node.right = self.deleteMinByNode(t.right)
            node.left = t.left

        node.count = 1 + self.sizeIt(node.left) + self.sizeIt(node.right)
        return node

    def contains(self, key):
        if self.get(key) is not None:
            return True
        return False

    def rangeCount(self, low, high):
        if self.contains(high):
            return self.rank(high) - self.rank(low) + 1
        else:
            return self.rank(high) - self.rank(low)

