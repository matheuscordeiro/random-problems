def solution(number):
    a = 1
    b = 2
    total = b
    while a+b <= number:
        value = a + b
        if value % 2 == 0:
            total += value

        a, b = b, value

    return total


if __name__ == "__main__":
    print(solution(4000000))