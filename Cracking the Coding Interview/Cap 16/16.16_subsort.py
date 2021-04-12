def subsort(array):
    sorted_array = sorted(array)
    m = n = -1
    is_init = True
    for key, value in enumerate(array):
        if value != sorted_array[key]:
            if is_init:
                m = key
                is_init = False
            n = key

    return (m, n)


if __name__ == "__main__":
    array = [1,2,4,7,10,11,12,16,18,19]
    print(subsort(array))