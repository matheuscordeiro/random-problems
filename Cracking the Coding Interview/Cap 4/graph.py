
class Node:

    def __init__(self, value):
        self.adjacents = []
        self.visited = False
        self.value = value

    def add_adjacent(self, node):
        self.adjacents.append(node)


class Graph:

    def __init__(self, *args, **kwargs):
        self.nodes = []
    
    def add_node(self, node: Node):
        self.nodes.append(node)
