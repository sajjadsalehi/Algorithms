from BST import *

bst = Bst()

bst.put("h", "h")
bst.put("c", "c")
bst.put("a", "a")
bst.put("r", "r")
bst.put("x", "x")
bst.put("e", "e")
bst.put("z", "z")
bst.put("s", "s")

print(bst.min())
print(bst.max())
print(bst.floor("j"))
print(bst.size())
print(bst.rank("z"))
print(bst.keys())
bst.deleteMin()
bst.delete("s")
print(bst.keys())

