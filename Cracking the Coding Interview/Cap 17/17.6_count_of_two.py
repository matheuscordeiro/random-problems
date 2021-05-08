
def count_by_number(number:int, cash:dict):
    count = 0
    value = number
    while value > 0:
        if value in cash:
            cash[number] = cash[value] + count
            return cash[number]

        if value % 10 == 2:
            count += 1

        value = value // 10
    
    cash[number] = count
    return count


def count_of_two(number):
    count = 0
    cash = {}
    for i in range(2, number+1):
        count += count_by_number(i, cash)

    return count


if __name__ == "__main__":
    print(count_of_two(23))