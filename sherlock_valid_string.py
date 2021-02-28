
# Sherlock and the Valid String
# Difficulty: Medium

def isValid(s):
    frequency = {}
    count_frequency = {}
    for character in s:
        frequency[character] = frequency.get(character, 0) + 1

    for _, value in frequency.items():
        count_frequency[value] = count_frequency.get(value, 0) + 1
    
    if len(count_frequency) == 1:
        return 'YES'
    elif len(count_frequency) == 2:
        freq = list(count_frequency.items())
        major = max(freq[0][0], freq[1][0])
        minor = min(freq[0][0], freq[1][0])

        if (
            (minor == 1 and count_frequency[1] == 1) or 
            (count_frequency[major] == 1 and major - minor == 1)
        ):
            return 'YES'
    
    return 'NO'


if __name__ == '__main__':
    print(isValid('abccc'))