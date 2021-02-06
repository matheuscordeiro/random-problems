from graph import Node

# Depth-First Search (DFS)


def search(root: Node):
    root.visited = True
    print(root.value)
    for adjacent in root.adjacents:
        if not adjacent.visited:
            search(adjacent)
