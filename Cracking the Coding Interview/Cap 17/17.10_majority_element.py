def get_candidate(array):
    majority = count = 0
    for value in array:
        if count == 0:
            majority = value
            count += 1
        elif value == majority:
            count += 1
        else:
            count -= 1

    return majority


def find_majority(array):
    candidate = get_candidate(array)
    frenquency = array.count(candidate)
    return candidate if frenquency > len(array)/2 else -1


if __name__ == "__main__":
    array = [1,2,5,9,5,9,5,5,5]
    print(find_majority(array))
