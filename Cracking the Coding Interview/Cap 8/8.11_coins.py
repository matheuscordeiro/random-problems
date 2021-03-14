def count_coins(coins, start, value, hash_table):
    if hash_table.get(value) and hash_table[value].get(start):
        return hash_table[value][start]

    if start == len(coins) - 1:
        return 1

    count = 0
    i = 0
    while i * coins[start] <= value:
        count += count_coins(coins, start+1, value - (i*coins[start]), hash_table)
        i += 1

    if not hash_table.get(value):
        hash_table[value] = {}
    
    hash_table[value][start] = count
    return count


if __name__ == "__main__":
    coins = [25, 10, 5, 1]
    hash_table = {}
    print(count_coins(coins, 0, 50, hash_table))