class Node:

    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.visited = False


MAX_VALUE = 1000000

def find_in_order_successor(root: Node, input_node: Node):
    if not input_node:
        return None

    root.visited = True
    queue = [root]
    minimal = MAX_VALUE
    minimal_node = None
    while queue:
        node = queue.pop(0)
        node.visited = True
        if node.value > input_node.value and node.value < minimal:
            minimal = node.value
            minimal_node = node

        if node.left and not node.left.visited:
            node.left.visited = True
            queue.append(node.left)

        if node.right and not node.right.visited:
            node.right.visited = True
            queue.append(node.right)

    return minimal_node


if __name__ == "__main__":
    a = Node(11)
    b = Node(14)
    c = Node(12, a, b)
    d = Node(5)
    e = Node(9, d, c)
    f = Node(25)
    g = Node(20, e, f)
    print(find_in_order_successor(g, b).value)
    