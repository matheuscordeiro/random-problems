def get_signal(value: int):
    # return 0 if is positive and 1 is negative
    return (value >> 31) & 1


def flip(value):
    return value ^ 1


def number_max(a: int, b: int):
    signal_a = get_signal(a-b)
    return a * flip(signal_a) + b * signal_a


if __name__ == "__main__":
    print(number_max(4, 5))