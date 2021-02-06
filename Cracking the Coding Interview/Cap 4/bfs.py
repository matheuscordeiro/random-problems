from graph import Node

# Breadth-First Search (BFS)

def search(root: Node):
    queue = []
    queue.append(root)
    root.visited = True
    print(root.value)  # visit
    while queue:
        node = queue.pop(0)
        for adjacent in node.adjacents:
            if not adjacent.visited:
                adjacent.visited = True
                print(adjacent.value)  # visit
                queue.append(adjacent)
