# Lily's Homework
# Difficulty: Medium

def lilysHomework(arr):
    positions_order = {}
    positions_reverse = {}
    arr_copy = []
    for key, value in enumerate(arr):
        positions_order[value] = key
        positions_reverse[value] = key
        arr_copy.append(value)

    sorted_arr = sorted(arr)
    size_arr = len(arr)
    swap_order = swap_reverse = 0
    for key in range(size_arr):

        # order
        value_order = sorted_arr[key]
        if value_order != arr[key]:
            tmp_value = arr[key]
            tmp_position = positions_order[value_order]
            # swap
            arr[key] = value_order
            positions_order[value_order] = key
            arr[tmp_position] = tmp_value
            positions_order[tmp_value] = tmp_position
            swap_order += 1

        # reverse
        value_reverse = sorted_arr[size_arr-key-1]
        if value_reverse != arr_copy[key]:
            tmp_value = arr_copy[key]
            tmp_position = positions_reverse[value_reverse]
            # swap
            arr_copy[key] = value_reverse
            positions_reverse[value_reverse] = key
            arr_copy[tmp_position] = tmp_value
            positions_reverse[tmp_value] = tmp_position
            swap_reverse += 1

    return min(swap_order, swap_reverse)


if __name__ == "__main__":
    array = [3, 4, 2, 5, 1]
    print(lilysHomework(array))