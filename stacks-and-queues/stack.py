class Stack:
  def __init__(self, data=None):
    self.head = Node(data) if data else data
    self.length = 1 if self.head != None else 0
  
  def push(self, data):
    next = Node(data, self.head)
    self.head = next
    self.length += 1

  def pop(self):
    if self.head:
      current = self.head
      self.head = current.next
      current.next = None
      self.length -= 1
    else:
      return None
    return current.data

  def peek(self):
    return self.head.data if self.head else "Empty"

  def __repr__(self):
    if self.head:
      current = self.head
      repr = [current.data]
      while current.next:
        current = current.next
        repr.append(current.data)
    else:
      repr = []
    return str(repr)

class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next