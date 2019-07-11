# Adjacency List DataStructure
## This is a basic DataStructure that probably has adaptations for all types of graphs.
### Make all possible possibilities, in this case 4?.
#### Combination1: For Undirected and Unweighted Graph
#### Combination2: For Directed and Unweighted Graph 
#### Combination3: For Undirected and Weighted Graph
#### Combination4: For Directed and Weighted Graph

class AdjacencyList(object):

    def __init__(self, key):
        self.id = key
        self.linked_to = dict()

    def add_connection(self, another_element, weight=0):
        self.linked_to[another_element] = weight

    def get_connections(self):
        return self.linked_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, another_element):
        return self.linked_to[another_element]    