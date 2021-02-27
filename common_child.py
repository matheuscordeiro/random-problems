

# Commom child
# Difficulty: Medium

def commonChild(s1, s2):
    previous_row = [0] * (len(s1) + 1)
    current_row = [0] * (len(s1) + 1)

    for value_i in s1:
        previous_row, current_row = current_row, previous_row
        for key, value_j in enumerate(s2, 1):
            if value_i == value_j:
                current_row[key] = previous_row[key-1] + 1
            else:
                current_row[key] = max(previous_row[key], current_row[key-1])

    return current_row[-1]


if __name__ == "__main__":
    print(commonChild('HARRY', 'HARRY'))
