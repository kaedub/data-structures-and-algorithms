class LinkedList():
  """This is a general purpose linked list class that can be subclassed"""
  def __init__(self, node):
    self.head = node
    self.tail = node

  def find(self, node):
    pass

  def push(self, node):
    self.tail.next = node
    self.tail = node

  def pop(self):
    popped = self.tail
    self.tail = self.tail.previous
    self.tail.next = None
    return popped
  
  def enqueue(self, node):
    pass

  def dequeue(self):
    pass


class DoubleLL():
  def __init__(self, data):
    if isinstance(data, list):
      self.head = DoubleNode(data[0], None, None)
      previous = self.head
      for i in range(1,len(data)):
        # create the new node with a reference to previous node
        node = DoubleNode(data[i], None, previous)
        # set previous node with a reference to the next node
        previous.next = node
        # the node has been added, this one is now the previous to the next one
        previous =  node




class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

class DoubleNode():
  def __init__(self, data, next, previous):
    self.data = data
    self.next = next
    self.previous = previous