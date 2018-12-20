from tree import Tree, createIntTree


t = createIntTree()

print('show', t.root.show())
print('sum', t.root.sum())
print('find 3', t.root.find(3) != False)
print('evens', t.root.evens())
print('min depth', t.root.min_depth())