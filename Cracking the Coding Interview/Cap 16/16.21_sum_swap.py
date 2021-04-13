def sum_swap(array1, array2):
    sum1 = sum2 = 0
    for value in array1:
        sum1 += value

    register = {}
    for value in array2:
        sum2 += value
        register[value] = True

    difference = abs(sum1-sum2)
    for value in array1:
        if value < difference and register.get(difference-value):
            return value, difference-value

    return -1


if __name__ == "__main__":
    array1 = [4,1,2,1,1,2]
    array2 = [3,6,3,3]
    print(sum_swap(array1, array2))