def next_number(number):
    # finding the first 0 with 1 in its right of
    n = number
    count_zeros = count_ones = 0
    while (n & 1) == 0 and n !=0:
        count_zeros += 1
        n >>= 1

    while (n & 1) == 1:
        count_ones += 1
        n >>= 1

    p = count_ones + count_zeros
    number |= (1 << p)  # flip p (0 to 1)
    number &= ~0 << p   # clear right of p
    number |= (1 << count_ones-1) - 1  # add count_ones - 1 ones in right of p
    return number


def previous_number(number):
    # finding the first 1 with 0 in its right of
    n = number
    count_zeros = count_ones = 0
    while (n & 1) == 1:
        count_ones += 1
        n >>= 1

    while (n & 1) == 0:
        count_zeros += 1
        n >>= 1

    p = count_ones + count_zeros
    number &= ~0 << (p + 1)  # flip p (1 to 0)
    a = 1 << (count_ones + 1)
    b = a - 1
    c = b << (count_zeros - 1)
    number |= c
    return number


if __name__ == '__main__':
    print(previous_number(6))