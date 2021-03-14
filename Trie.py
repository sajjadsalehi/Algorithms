class Node:
    def __init__(self):
        self.value = None
        self.char = None
        self.left = None
        self.mid = None
        self.right = None


class Trie:
    def __init__(self):
        self.root = None

    def put(self, key, val):
        self.root = self.put1(self.root, key, val, 0)

    def put1(self, node, key, val, d):
        c = key[d]
        if node is None:
            node = Node()
            node.char = c
        if c < node.char:
            node.left = self.put1(node.left, key, val, d)
        elif c > node.char:
            node.right = self.put1(node.right, key, val, d)
        elif d < len(key) -1:
            node.mid = self.put1(node.mid, key, val, d+1)
        else:
            node.val = val
        return node

    def get(self, key):
        node = self.get1(self.root, key, 0)
        if node is None:
            return None
        return node.val

    def get1(self, node, key, d):
        if node is None:
            return None
        ch = key[d]
        if ch < node.char:
            return self.get1(node.left, key, d)
        elif ch > node.char:
            return self.get1(node.right, key, d)
        elif d < len(key)-1:
            return self.get1(node.mid, key, d+1)
        else:
            return node
