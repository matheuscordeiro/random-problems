from graph import Graph, Node



def has_route_bfs(node_a: Node, node_b: Node) -> bool:
    """BFS is often prefered if we wanted to find the shortest path
    between two nodes
    """
    if node_a == node_b:
        return True
    
    queue = []
    node_a.visited = True
    queue.append(node_a)
    while queue:
        node = queue.pop(0)
        for adjacent in node.adjacents:
            if not adjacent.visited:
                if adjacent == node_b:
                    return True
                
                adjacent.visited = True
                queue.append(adjacent)
    return False


def has_route_dfs(node_a: Node, node_b: Node) -> bool:
    """DFS is often prefered if we want to visit every node
    """
    if node_a == node_b:
        return True
    
    node_a.visited = True
    for adjacent in node_a.adjacents:
        if has_route_bfs(adjacent, node_b):
            return True
    
    return False


if __name__ == "__main__":
    node_a = Node(10)
    node_b = Node(5)
    node_c = Node(2)
    node_d = Node(5)

    root = Node(30)
    root.add_adjacent(node_a)
    root.add_adjacent(node_b)
    node_a.add_adjacent(node_c)
    node_a.add_adjacent(node_d)

    print(has_route_dfs(node_b, node_c))
