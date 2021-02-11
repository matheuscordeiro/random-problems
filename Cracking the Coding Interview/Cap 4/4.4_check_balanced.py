from graph import Node


def _bigger_height(root: Node):
    if not root.adjacents:
        return 0

    height_left = _bigger_height(root.adjacents[0]) + 1
    height_right = 0
    if len(root.adjacents) > 1:
        height_right = _bigger_height(root.adjacents[1]) + 1

    if height_left == -1 or height_right == -1 or abs(height_left - height_right) > 1:
        return -1

    return max(height_left, height_right)

def check_balanced(root: Node):
    if _bigger_height(root) == -1:
        return False
    else:
        return True


if __name__ == "__main__":
    node_a = Node(10)
    node_b = Node(50)
    node_c = Node(9)
    node_d = Node(11)
    node_e = Node(45)
    node_f = Node(43)

    root = Node(30)
    root.add_adjacent(node_a)  # left
    root.add_adjacent(node_b)  # right
    node_a.add_adjacent(node_c)  # left
    node_a.add_adjacent(node_d)  # right
    node_b.add_adjacent(node_e)  # left
    node_e.add_adjacent(node_f)  # left

    print(check_balanced(root))
