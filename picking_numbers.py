# Picking numbers
# Difficulty: Easy

def pickingNumbers(a):
    frequency = {}
    for value in a:
        frequency[value] = frequency.get(value, 0) + 1

    maximum = 0
    for key, _ in frequency.items():
        count = frequency[key] + frequency.get(key+1, 0)
        maximum = max(maximum, count)

    return maximum


if __name__ == "__main__":
    array = [4, 6, 5, 3, 3, 1]
    print(pickingNumbers(array))
