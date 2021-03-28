# Pairs
# Difficulty: Medium

def pairs(k, arr):
    frequency = {}
    for value in arr:
        frequency[value] = frequency.get(value, 1)

    count = 0
    for value in arr:
        if frequency.get(value + k):
            count += 1

    return count


if __name__ == "__main__":
    array = [1, 5, 3, 4, 2]
    print(pairs(2, array))