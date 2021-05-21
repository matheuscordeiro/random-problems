def longest_word(words: list):
    frequency = {}
    for word in words:
        frequency[word] = True

    words = sorted(words, reverse=True, key=len)
    for word in words:
        if is_made_by(word, frequency, is_original=True):
            return word

    return ""


def is_made_by(word, frequency, is_original=False):
    if word in frequency and not is_original:
        return frequency[word]

    for i in range(1, len(word)):
        left = word[:i]
        right = word[i:]
        if frequency.get(left) and is_made_by(right, frequency):
            return True

    frequency[word] = False
    return False


if __name__ == "__main__":
    words = ["matheus", "ma", "th", "theus"]
    print(longest_word(words))
