
def remove_min(queue):
    frequency = {}
    min_value = queue[0]
    for value in queue:
        frequency[value] = frequency.get(value, 0) + 1
        if value < min_value:
            min_value = value

    for _ in range(frequency[min_value]):
        queue.remove(min_value)

    return min_value


def add_item(queue, item):
    queue.append(item*3)
    queue.append(item*5)
    queue.append(item*7)

def kth_multiple(k):
    queue = [1]
    for i in range(k):
        min_value = remove_min(queue)
        add_item(queue, min_value)

    return min_value


if __name__ == "__main__":
    print(kth_multiple(4))
