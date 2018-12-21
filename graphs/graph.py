from queue import Queue


class Graph:
  def __init__(self, nodes=None)  :
    self.nodes = set(nodes) if isinstance(nodes, list) else set()

  def _get_node(self):
    """Return a random Node instance"""
    for node in self.nodes:
      return node
    return None

  def get_nodes(self):
    """Return a list of Node instances for this graph"""
    nodes = []
    for node in self.nodes:
      nodes.append(node)
    return nodes

  def add_nodes(self, *nodes):
    """Add nodes to graph, accepts variable number of parameters"""
    if isinstance(nodes, tuple):
      for node in nodes:
        self.nodes.add(node)
    else:
      self.nodes.add(nodes)

  def remove_nodes(self, *nodes):
    """Remove nodes from graph, accepts variable number of parameters"""
    if isinstance(nodes, tuple):
      for node in nodes:
        self.nodes.remove(node)
    else:
      self.nodes.remove(nodes)

  def add_edge(self, node1, node2):
    """Add an edge between node1 and node2"""
    node1.add_edges(node2)
  
  def remove_edge(self, node1, node2):
    """Remove an edge between node1 and node2"""
    node1.remove_edges(node2)
    
  def runBFS(self, action):
    """Run breadth first search and use the given action function"""
    if len(self.nodes) > 0:
      self._get_node().traverseBFS(action)

  def runDFS(self, action):
    """Run depth first search and use the given action function"""
    if len(self.nodes) > 0:
      self._get_node().traverseDFS(action)


class Node:
  def __init__(self, data):
    self.data = data
    self.adjacent = set([])

  def get_adjacent(self):
    return list(self.adjacent)
  
  def add_edges(self, *nodes):
    """Add a variable number of edges between this node and the passed nodes"""
    for node in nodes:
      self.adjacent.add(node)
      node.adjacent.add(self)

  def remove_edges(self, *nodes):
    """Remove a variable number of edges between this node and the passed nodes"""
    for node in nodes:
      self.adjacent.remove(node)
      node.adjacent.remove(self)
    
  def traverseBFS(self, action=None):
    """General breadth first search, accepts a function as action to run while searching"""
    queue = Queue()
    visited = set([self])
    queue.put(self)
    
    while (queue.qsize()):
      current = queue.get()

      if action:
        action(current.data)
      
      for adj in current.adjacent:
        if adj not in visited:
          visited.add(adj)
          queue.put(adj)

  def traverseDFS(self, action=None):
    """General depth first search, accepts a function as action to run while searching"""
    stack = []
    visited = set([self])
    stack.append(self)
    
    while (len(stack)):
      current = stack.pop()

      if action:
        action(current.data)
      
      for adj in current.adjacent:
        if adj not in visited:
          visited.add(adj)
          stack.append(adj)


############################################
# Helper functions

def create_nodes(n):
  """Create n Nodes"""
  return list(map(lambda x: Node(chr(x+97)), range(n)))

# Create the following graph
#
#      A 
#     /  \
#    B -- C
#    | \  |
#    |  \ |
#    D -- E -- F

def create_graph1(nodes=None):
  """Create a graph with the given nodes"""
  # if isinstance(nodes, list):
  #   return Graph(nodes)
  
  a,b,c,d,e,f = create_nodes(6)

  a.add_edges(a,b)
  b.add_edges(a,c,d,e)
  c.add_edges(a,b,e)
  d.add_edges(b,e)
  e.add_edges(b,c,d,f)
  f.add_edges(e)

  return Graph([a,b,c,d,e,f])


# Create the following graph
#
#    A 
#    |
#    B -- C
#    | \
#    |  \ 
#    D -- E  

def create_graph2():
  """Create a graph with the given nodes"""
  a,b,c,d,e = create_nodes(5)

  a.add_edges(b)
  b.add_edges(a,c,d,e)
  c.add_edges(b)
  d.add_edges(b,e)
  e.add_edges(b,d)

  return Graph([a,b,c,d,e])