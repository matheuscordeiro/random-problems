from graph import Node


def check_bst(root: Node):
    if not root.adjacents:
        return True

    if root.adjacents[0].value > root.value or root.adjacents[1].value < root.value:
        return False

    return check_bst(root.adjacents[0]) and check_bst(root.adjacents[1])


if __name__ == "__main__":
    node_a = Node(10)
    node_b = Node(50)
    node_c = Node(9)
    node_d = Node(11)
    node_e = Node(45)
    node_f = Node(55)

    root = Node(30)
    root.add_adjacent(node_a)  # left
    root.add_adjacent(node_b)  # right
    node_a.add_adjacent(node_c)  # left
    node_a.add_adjacent(node_d)  # right
    node_b.add_adjacent(node_e)  # left
    node_b.add_adjacent(node_f)  # right

    print(check_bst(root))
