class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def height(root: Node):
    if not root or (not root.left and not root.right):
        return 0

    left = height(root.left) if root.left else 0
    right = height(root.right) if root.right else 0
    if left == -1 or right == -1 or abs(left-right) > 1:
        return -1

    return 1 + max(left, right)


def check_balanced(root: Node):
    if height(root) == -1:
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
    root.left = node_a  # left
    root.right = node_b  # right
    node_a.left = node_c  # left
    node_a.right = node_d  # right
    node_b.left = node_e  # left

    print(check_balanced(root))
