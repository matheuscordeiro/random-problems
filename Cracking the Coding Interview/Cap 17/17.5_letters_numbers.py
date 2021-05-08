def calculate_gap(array):
    gap = [0]
    numbers = letters = 0
    for value in array:
        if value.isdigit():
            numbers += 1
        else:
            letters += 1

        gap.append(numbers - letters)

    return gap
    

def find_position_longest_subarray(gap):
    positions = {"0": -1}
    i = j = max_distance = -1
    for key, value in enumerate(gap):
        if value in positions:
            distance = key - positions[value]
            if distance > max_distance:
                max_distance = distance
                i = positions[value]
                j = key
        else:
            positions[value] = key

    return i, j


def longest_subarray(array):
    gap = calculate_gap(array)
    print(gap)
    i, j = find_position_longest_subarray(gap)
    return array[i+1:j+1]



if __name__ == "__main__":
    array = ["a", "1", "c", "4", "5"]
    print(longest_subarray(array))