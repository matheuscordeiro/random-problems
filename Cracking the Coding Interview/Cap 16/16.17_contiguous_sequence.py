def contiguous_sequence(array):
    max_value = sum_value = 0
    for value in array:
        sum_value += value
        if sum_value > max_value:
            max_value = sum_value
        elif sum_value < 0:
            sum_value = 0

    return max_value


if __name__ == "__main__":
    array = [2, -8, 3, -2, 4, -10]
    print(contiguous_sequence(array))