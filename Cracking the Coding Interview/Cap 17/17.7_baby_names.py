
class Node:

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.neighborhood = []
        self.visited = False

    def add_neighbor(self, node):
        self.neighborhood.append(node)


class Graph:

    def __init__(self):
        self.nodes = []
        self.ref_nodes = {}

    def add_node(self, node):
        self.ref_nodes[node.name] = node
        self.nodes.append(node)

    def conect_nodes(self, name_node1, name_node2):
        node1 = self.ref_nodes[name_node1]
        node2 = self.ref_nodes[name_node2]
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)


def create_graph(names):
    graph = Graph()
    for name, value in names:
        graph.add_node(Node(name, value))

    return graph


def conect_edges(grap, synonyms):
    for name1, name2 in synonyms:
        grap.conect_nodes(name1, name2)


def get_frequencies(names: list, synonyms: list):
    grap = create_graph(names)
    conect_edges(grap, synonyms)
    frequencies = {}
    for name, _ in names:
        node = grap.ref_nodes[name]
        if not node.visited:
            frequencies[name] = dfs(node)

    return frequencies


def dfs(root: Node):
    root.visited = True
    count = root.value
    for node in root.neighborhood:
        if not node.visited:
            count += dfs(node)
            
    return count


if __name__ == "__main__":
    names = [("John", 10), ("Jon", 3), ("Davis", 2), ("Kari", 3), ("Johnny", 11), ("Carlton", 8), ("Carleton", 2), ("Jonathan", 9), ("Carrie", 5)]
    synonyms = [("Jonathan", "John"), ("Jon", "Johnny"), ("Johnny", "John"), ("Kari", "Carrie"), ("Carleton", "Carlton")]
    print(get_frequencies(names, synonyms))