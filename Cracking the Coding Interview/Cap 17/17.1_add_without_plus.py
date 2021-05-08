def add_without_plus(a, b):
    if not b:
        return a

    no_carry = a ^ b # XOR
    carry = (a & b) << 1 # AND SHIFTED BY 1
    return add_without_plus(no_carry, carry)


if __name__ == "__main__":
    print(add_without_plus(10, 0))