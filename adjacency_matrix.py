# Adjacency Matrix DataStructure
## This is a basic DataStructure that probably has adaptations for all types of graphs.
### Make all possible possibilities, in this case 4?.
#### Combination1: For Undirected and Unweighted Graph
#### Combination2: For Directed and Unweighted Graph 
#### Combination3: For Undirected and Weighted Graph
#### Combination4: For Directed and Weighted Graph

class AdjacencyMatrix(object):

    def __init__(self, size):
        self.matrix = []
        for index in range(size):
            self.matrix.append([0 for index in range(size)])
        self.size = size

    def add_connection(self, index_1, index_2):
        if index_1 == index_2:
            return 
        self.matrix[index_1][index_2] = 1
        self.matrix[index_2][index_1] = 1

    def remove_edge(self, index_1, index_2):
        if self.matrix[index_1][index_2] == 0:
            return
        self.matrix[index_1][index_2] = 0
        self.matrix[index_2][index_1] = 0