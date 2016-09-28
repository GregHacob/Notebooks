class Kruskal(object):
    def __init__(self, graph):
     self.graph = graph
     self.connections = dict()
     self.numberOfConnections = dict()
    
    def make_set(self, node):
     self.connections[node] = node
     self.numberOfConnections[node] = 0

    def find(self, node):
     if self.connections[node] != node:
        self.connections[node] = self.find(self.connections[node])
     return self.connections[node]

    def connect_nodes(self, from_node, to_node):
     node1 = self.find(from_node)
     node2 = self.find(to_node)
     if node1 != node2:
        if self.numberOfConnections[node1] > self.numberOfConnections[node2]:
            self.connections[node2] = node1
        else:
            self.connections[node1] = node2
            if self.numberOfConnections[node1] == self.numberOfConnections[node2]: self.numberOfConnections[node2] += 1

    def buildMST(self):
      for node in self.graph.nodes:
        self.make_set(node)  

      minimum_spanning_tree = []

      self.graph.edges.sort(key=lambda x: x.value)
      for edge in self.graph.edges:
            if self.find(edge.node_from) != self.find(edge.node_to):
                self.connect_nodes(edge.node_from, edge.node_to)
                minimum_spanning_tree.append(edge)
      return minimum_spanning_tree  
      
    def adjacencyList(self, MSTList):
     mst_dict = dict()
     for i in range(len(MSTList)):
         node1 = MSTList[i].node_from.value
         node2 = MSTList[i].node_to.value
         edge_value = MSTList[i].value
         if node1 not in mst_dict:   
            mst_dict[node1] = [(node2, edge_value)]
         else:
            coonect_list = mst_dict[node1]
            coonect_list.append((node2, edge_value))
            mst_dict[node1] = coonect_list
          
         if node2 not in mst_dict:   
            mst_dict[node2] = [(node1, edge_value)]
         else:
            coonect_list = mst_dict[node2]
            coonect_list.append((node1, edge_value))
            mst_dict[node2] = coonect_list 
            
     return mst_dict       

