class Node:

    def __init__(self, key, value, red=False):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = red


class RedBlackBST:

    def __init__(self):
        self.root = None

    def isRed(self, node):
        if node is None:
            return False
        return node.color

    def rotateLeft(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = True
        return x

    def rotateRight(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = True
        return x

    def flipColors(self, node):
        node.color = True
        node.left.color = False
        node.right.color = False

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
            return Node(key, value, True)
        if key < node.key:
            node.left = self.putIt(node.left, key, value)
        elif key > node.key:
            node.right = self.putIt(node.right, key, value)
        else:
            node.value = value

        if self.isRed(node.right) and not self.isRed(node.left):
            node = self.rotateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node = self.rotateRight(node)
        if self.isRed(node.left) and self.isRed(node.right):
            self.flipColors(node)

        return node

