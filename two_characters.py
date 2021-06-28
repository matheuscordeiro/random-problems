def alternate(s):
    letters = {value: True for value in s}
    items = letters.items()
    options = []
    frequency = {}
    for key, _ in items:
        for key2, _ in items:
            if key2 != key and not frequency.get(f"{key}{key2}"):
                options.append((key, key2))
                frequency[f"{key}{key2}"] = True
                frequency[f"{key2}{key}"] = True


    max_lenght = 0
    for char1, char2 in options:
        current = 0
        char_before = None
        flag = True
        for key, value in enumerate(s):
            if value == char1 or value == char2:
                current += 1
                if char_before == value:
                    flag = False
                    break

                char_before = value

        if flag:
            max_lenght = max(max_lenght, current)

    return max_lenght


if __name__ == "__main__":
    # s = "beabeefeab"
    s = "abaacdabd"
    # s = "asvkugfiugsalddlasguifgukvsa"
    print(alternate(s))
    