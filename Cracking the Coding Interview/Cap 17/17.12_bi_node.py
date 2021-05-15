class SubList:

    def __init__(self, head=None, tail=None) -> None:
        self.head = head
        self.tail = tail


class Node:

    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def update_linked_list(before:Node, next:Node):
    before.right = next
    next.left = before


def build_linked_list(root: Node):
    if not root:
        return None

    right:SubList = build_linked_list(root.right)
    left:SubList = build_linked_list(root.left)

    if right:
        update_linked_list(root, right.head)

    if left:
        update_linked_list(left.tail, root)

    head = left.head if left else root
    tail = right.tail if right else root
    return SubList(head, tail)


if __name__ == "__main__":
    a = Node(0, None, None)
    b = Node(1, a, None)
    c = Node(3, None, None)
    d = Node(2, b, c)
    e = Node(6, None, None)
    f = Node(5, None, e)
    root = Node(4, d, f)
    build_linked_list(root)