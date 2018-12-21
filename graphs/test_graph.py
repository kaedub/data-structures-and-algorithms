from graph import Graph, Node, create_graph1, create_graph2, create_nodes

GRAPH1 = create_graph2()
GRAPH2 = create_graph2()

def _get_node_list(graph):
  return list(map(lambda n: n.data, graph.get_nodes()))

def get_bfs():
  """Tests Graph.getBFS should return of nodes data"""
  nodes = []
  GRAPH2.runBFS(lambda n: nodes.append(n))
  return nodes

def get_dfs():
  """Tests Graph.getDFS should return of nodes data"""
  nodes = []
  GRAPH2.runDFS(lambda n: nodes.append(n))
  return nodes


def add_nodes():
  """Tests Graph.add_nodes method should add a node from the graph"""
  h = Node('h')
  i = Node('i')
  GRAPH2.add_nodes(h,i)
  
  return _get_node_list(GRAPH2)

def add_node():
  """Tests Graph.add_nodes method should add a node from the graph"""
  j = Node('j')
  GRAPH2.add_nodes(j)
  
  return _get_node_list(GRAPH2)

def remove_nodes():
  """Tests Graph.remove_nodes method should remove a node from the graph"""
  nodes = GRAPH2.get_nodes()
  GRAPH2.remove_nodes(nodes[0], nodes[1])
  return _get_node_list(GRAPH2)

def remove_node():
  """Tests Graph.remove_nodes method should remove a node from the graph"""
  n1 = GRAPH2._get_node()
  GRAPH2.remove_nodes(n1)
  return _get_node_list(GRAPH2)

def add_edge():
  """Tests Graph.add_edge method should add an edge between 2 nodes"""
  x = Node('x')

  GRAPH2.add_nodes(x)
  GRAPH2._get_node().add_edges(x)

  return _get_node_list(GRAPH2)

def add_edges():
  """Tests Graph.add_edge method should add an edge between 2 nodes"""
  x,y,z = Node('x'), Node('y'), Node('z')

  GRAPH2.add_nodes(x,y,z)
  GRAPH2._get_node().add_edges(x,y,z)

  return _get_node_list(GRAPH2)

def remove_edge():
  """Tests Graph.remove_edge method should remove an edge between 2 nodes"""
  GRAPH2.remove_nodes(GRAPH2._get_node())
  return _get_node_list(GRAPH2)

def remove_edges():
  """Tests Graph.remove_edge method should remove an edge between 2 nodes"""
  nodes = GRAPH2.get_nodes()
  GRAPH2.remove_nodes(*nodes[0:3])
  return _get_node_list(GRAPH2)

print('> BFS      get_bfs should return a list:                                     ', get_bfs())
print('> DFS      get_dfs should return a list:                                     ', get_dfs())
print('> ADD      add_nodes should add multiple nodes and return a list:            ', add_nodes())
print('> ADD      add_node should add a single node and return a list:              ', add_node())
print('> REMOVE   remove_nodes should remove multiple nodes and return a list:      ', remove_nodes())
print('> REMOVE   remove_node should remove a single node and return a list:        ', remove_node())
print('> ADD      add_edge should add an edge between nodes and return a list:      ', add_edge())
print('> ADD      add_edges should add an edge between nodes and return a list:     ', add_edges())
print('> REMOVE   remove_edge should add an edge between nodes and return a list:   ', remove_edge())
print('> REMOVE   remove_edges should add an edge between nodes and return a list:  ', remove_edges())
