from graph import Node


def list_depths(root):
    queue = []
    array = []
    linked_lists = [[root.value]]
    queue.append(root)
    queue.append(None)
    while queue:
        node = queue.pop(0)
        if node:
            for adjacent in node.adjacents:
                array.append(adjacent.value)
                queue.append(adjacent)
        elif queue:
            queue.append(None)
            linked_lists.append(array)
            array = []
        else:
            break

    return linked_lists


if __name__ == "__main__":
    node_a = Node(10)
    node_b = Node(50)
    node_c = Node(9)
    node_d = Node(11)
    node_e = Node(55)

    root = Node(30)
    root.add_adjacent(node_a)  # left
    root.add_adjacent(node_b)  # right
    node_a.add_adjacent(node_c)  # left
    node_a.add_adjacent(node_d)  # right
    node_b.add_adjacent(node_e)  # right

    print(list_depths(root))
