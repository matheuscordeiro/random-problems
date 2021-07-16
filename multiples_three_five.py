def solution(a):
    total = 0
    for i in range(1, a):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total


if __name__ == "__main__":
    print(solution(1000))