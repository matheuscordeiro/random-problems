import math


numbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twelve",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

labels = {
    1: "billion",
    2: "million",
    3: "thousand"
}


def _english_to_three_places(number: int):
    digits = len(str(number))
    multiple = math.pow(10, digits-1)
    rest = number % multiple
    if digits == 1:
        return numbers[number]
    elif digits == 2: 
        if numbers.get(number):
            return numbers[number]
        else:
            value = number - rest
            name = _english_to_three_places(int(rest))
            return f"{numbers.get(value)} {name}"
    else:  # 3 digits
        value = number // multiple
        name = _english_to_three_places(int(rest))
        return f"{numbers.get(value)} hundred {name}"


def english_int(number: int):
    name = ""
    value = 1000000000 # billion
    count = 1
    while value >= 1:
        rest = number // value
        if rest > 0:
            name += _english_to_three_places(int(rest))
            if labels.get(count):
                name = f"{name} {labels.get(count)} "

            number %= value

        value /= 1000
        count += 1

    return name


if __name__ == "__main__":
    print(english_int(120156))
