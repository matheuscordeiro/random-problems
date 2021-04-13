import string


PHONE = {
    "0": "",
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def t9(number: str, words):
    return map_number_words(words).get(number, [])


def convert_digit_to_letter():
    letters = {}
    for letter in string.ascii_lowercase:
        for key, value in PHONE.items():
            if letter in value:
                letters[letter] = key

    return letters


def map_number_words(words):
    letters = convert_digit_to_letter()
    number_words = {}
    for word in words:
        number = ""
        for letter in word:
            number += letters[letter]
        
        if number_words.get(number):
            number_words[number].append(word)
        else:
            number_words[number] = [word]

    return number_words
        


if __name__ == "__main__":
    words = [
        "tree",
        "used",
        "have",
        "what"
    ]
    print(t9("8733", words))