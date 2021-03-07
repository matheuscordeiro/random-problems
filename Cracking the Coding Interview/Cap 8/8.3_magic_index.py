
# Search binary algorithm

def find_magic_index(array, start, end):
    if start > end:
        return -1

    middle = int((start + end) / 2)
    if array[middle] == middle:
        return middle
    elif array[middle] < middle:
        return find_magic_index(array, middle + 1, end)
    else:
        return find_magic_index(array, start, middle-1)


if __name__ == '__main__':
    array = [-40,-20,-1,1,2,3,5,7,9,12,13]
    print(find_magic_index(array, 0, 10))