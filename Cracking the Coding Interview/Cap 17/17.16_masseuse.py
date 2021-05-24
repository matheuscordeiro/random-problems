def highest_minutes(array, pos, cache):
    if pos >= len(array):
        return 0

    if pos in cache:
        return cache[pos]

    next_two = next_three = array[pos]
    next_two += highest_minutes(array, pos+2, cache)
    next_three += highest_minutes(array, pos+3, cache)
    cache[pos] = max(next_two, next_three)
    return cache[pos]


if __name__ == "__main__":
    cache = {}
    array = [30, 15, 60, 75, 45, 15, 15, 45]
    print(highest_minutes(array, 0, cache))
    