from graph import Node


def build_graph(array):
    size_array = len(array)
    pos = int(size_array/2)
    root = Node(array[pos])
    
    if size_array == 1:
        return root

    left = build_graph(array[:pos])
    if left:
        root.add_adjacent(left)
    
    if size_array > 2:
        right = build_graph(array[pos+1:])
        if right:
            root.add_adjacent(right)

    return root


if __name__ == "__main__":
    array = [1,2,3,4,5]
    build_graph(array)
