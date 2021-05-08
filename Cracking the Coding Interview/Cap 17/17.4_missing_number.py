def get_bit(number, colunm):
    result = number & (1 << colunm)
    return 1 if result else 0


def find_missing_number_by_bit(array, colunm):
    if colunm >= 100:  # max int in array
        return 0

    bit_one = []
    bit_zero = []
    for number in array:
        if get_bit(number, colunm):
            bit_one.append(number)
        else:
            bit_zero.append(number)

    if len(bit_zero) <= len(bit_one):  # then the number is even
        value = find_missing_number_by_bit(bit_zero, colunm+1)
        return value << 1
    else:
        value = find_missing_number_by_bit(bit_one, colunm+1)
        return (value << 1) | 1

def find_missing_number(array):
    return find_missing_number_by_bit(array, 0)  # least significant bit


if __name__ == "__main__":
    array = [0,1,2,3,4,6]
    print(find_missing_number(array))
