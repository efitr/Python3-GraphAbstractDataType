# Adjacency List DataStructure
from linkedlist import LinkedList, Node
class AdjacencyList(object):

    def __init__(self, init_size):
        self.nodes = [LinkedList() for i in range(init_size)
        