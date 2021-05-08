import random

def shuffle(cards):
    for i in range(len(cards)):
        rand_value = random.randint(0, i)
        temp = cards[i]
        cards[i] = cards[rand_value]
        cards[rand_value] = temp


if __name__ == "__main__":
    cards = [1,2,3,4,5,6,7,8,9,10]
    shuffle(cards)
    print(cards)
