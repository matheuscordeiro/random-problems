import math


def factorial_zeros(num):
    value = math.factorial(num)
    trailing_zeros = 0
    while value % 10 == 0:
        trailing_zeros += 1
        value /= 10

    return trailing_zeros


if __name__ == "__main__":
    print(factorial_zeros(3))