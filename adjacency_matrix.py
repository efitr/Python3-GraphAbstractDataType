# Adjacency Matrix DataStructure

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