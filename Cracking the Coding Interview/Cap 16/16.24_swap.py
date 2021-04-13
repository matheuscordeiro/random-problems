def all_pairs(array, sum_value):
    occurrences  = {}
    register = {}
    pairs = []
    for key, value in enumerate(array):
        look_for = sum_value - value
        position = occurrences.get(look_for)
        if position is not None and not register.get(f"{key},{position}"):
            pairs.append((look_for, value))
            register[f"{key},{position}"] = True
            register[f"{position},{key}"] = True
        
        occurrences[value] = key

    return pairs


if __name__ == "__main__":
    array = [4,5,9,10,2,3,15,12,1,0, -1]
    print(all_pairs(array, 4))