def shortest_supersequence(short, array):
    positions = create_close_positions(short, array)
    return find_shortest_distance(positions, len(array))

def create_close_positions(short, array) -> dict:
    positions_each_short_value = {}
    for s in short:
        positions_each_short_value[s] = update_positions(array, s)

    return positions_each_short_value


def update_positions(array, value) -> list:
    positions = [-1]*len(array)
    last = -1
    for i in range(len(array)-1, -1, -1):
        if array[i] == value:
            last = i
        positions[i] = last
    
    return positions


def find_shortest_distance(positions, size):
    best_start = best_size = -1
    for i in range(size):
        max_diff = -1
        for _, array in positions.items():
            if array[i] == -1:
                max_diff = -1
                break
            max_diff = max(max_diff, array[i])

        if max_diff == -1:
            continue

        if best_start == -1:
            best_size = max_diff-i
            best_start = i
        elif best_size > max_diff-i:
            best_size = max_diff-i
            best_start = i

    return best_start, best_size


if __name__ == "__main__":
    array = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
    short = [1,5,9]
    print(shortest_supersequence(short, array))

        
