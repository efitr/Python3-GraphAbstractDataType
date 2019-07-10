# Adjacency List DataStructure
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