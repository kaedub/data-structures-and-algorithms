from queue import Queue

class Tree:
    def __init__(self, root):
        self.root = root
    
    def find(self, val):
        self.root.find(val)

    def show(self):
        self.root.show()

class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

    def push(self, node):
        self.children.append(node)

    def find(self, val):
        toVisitStack = [self]
        while len(toVisitStack):
            current = toVisitStack.pop()

            if current.val == val:
                return current
            
            for child in current.children:
                toVisitStack.append(child)

    def show(self):
        output = [self.val]
        for child in self.children:
            output += child.show()
        return output

class IntNode(Node):
    def sum(self):
        output = self.val
        for child in self.children:
            output += child.sum()
        return output

    def evens(self):
        output = [self.val] if self.val%2 == 0 else []
        for child in self.children:
            output += child.evens()
        return output

    def min_depth(self):
        pass
        
    def max_depth(self):
        pass



def createIntTree():
    a = IntNode(1, 
        [
            IntNode(2, 
                [IntNode(4), IntNode(5)]
            ), 
            IntNode(3, 
                [
                    IntNode(6), 
                    IntNode(7),
                    IntNode(8, [IntNode(9)])
                ]
            )
        ]
    )

    tree = Tree(a)

    return tree
