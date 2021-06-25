import math

def calc_hash(password):
    total = 0
    n = len(password)
    for key, character in enumerate(password):
        total += ord(character) * math.pow(131, n-key-1)

    return str(int(total % (math.pow(10, 9) + 7)))

def hashes_friendly(password, current: dict):
    start = ord("a")
    end = start + 25
    while start <= end:
        current[calc_hash(f"{password}{chr(start)}")] = 1
        start += 1

    start = ord("A")
    end = start + 25
    while start <= end:
        current[calc_hash(f"{password}{chr(start)}")] = 1
        start += 1


def check(events: list):
    current = {}
    result = []
    for operation, password in events:
        if operation == "setPassword":
            current = {}
            current[calc_hash(password)] = 1
            hashes_friendly(password, current)
        else: 
            result.append(current.get(password, 0))

    return result


if __name__ == "__main__":
    events = [
        ("setPassword", "000A"),
        ("authorize", "108738450"),
        ("authorize", "108738449"),
        ("authorize", "244736787"),
    ]
    # events = [
    #     ("setPassword", "1"),
    #     ("setPassword", "2"),
    #     ("setPassword", "3"),
    #     ("authorize", "49"),
    #     ("authorize", "50")
    # ]
    print(check(events))