class Queue:
  def __init__(self, data=None):
    self.head = Node(data) if data != None else data
    self.tail = self.head
    self.length = 1 if self.head != None else 0
  
  def enqueue(self, data=None):
    next = Node(data)
    if self.head == None:
      self.head = next
      self.tail = next
    else:
      current = self.tail
      current.next = next
      self.tail = next
    self.length += 1


  def dequeue(self):
    current = self.head
    if self.head:
      self.head = current.next
    else:
      return None
    return current.data

  def peek(self):
    return "Empty" if self.head == None else self.head.data

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