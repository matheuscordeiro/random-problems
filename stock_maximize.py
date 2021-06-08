def stockmax(prices):
    sold = prices[len(prices)-1]
    profit = current = 0
    for i in range(len(prices)-2, -1, -1):
        if sold - prices[i] + current >= current:
            profit += sold - prices[i]
        else:
            sold = prices[i]
            current = 0

    return profit


if __name__ == "__main__":
    # prices = [5,4,3,4,5]
    # prices = [1,2,100]
    # prices = [2,1]
    # prices = [1,3,1,2]
    prices = [1,2,3,4]
    print(stockmax(prices))
