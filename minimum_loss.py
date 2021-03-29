# Minimum Loss
# Difficulty: Medium

import math


def minimumLoss(price):
    positions = {}
    for key, value in enumerate(price):
        positions[value] = key

    price = sorted(price)
    loss = math.pow(10, 16)
    for key in range(len(price)-1):
        if positions[price[key]] > positions[price[key+1]]:
            loss = min(loss, price[key+1] - price[key])
            if loss == 1:
                return 1

    return loss


if __name__ == "__main__":
    array = [20, 7, 8, 2, 5]
    print(minimumLoss(array))
