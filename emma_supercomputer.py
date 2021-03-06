
# Ema's Supercomputer
# Difficulty: Medium

def twoPluses(grid):
    len_string = len(grid[0])
    len_grid = len(grid)
    count = []
    positions = []
    for i in range(len_grid):
        for j in range(len_string):
            aux = 0
            if grid[i][j] == 'G':
                area = 1
                while (
                    i-aux >= 0 and j-aux >= 0 and i+aux < len_grid and j+aux < len_string and 
                    grid[i][j-aux] == 'G' and grid[i-aux][j] == 'G' and grid[i][j+aux] == 'G' and grid[i+aux][j] == 'G'
                ):
                    if aux:
                        area += 4
                    count.append(area)
                    current = [(i,j-aux), (i-aux,j), (i,j+aux), (i+aux,j)]
                    positions.append(current)  
                    aux += 1              

    max_mult = 0
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    row = 0
    col = 1
    for i in range(len(count)-1):
        for j in range(i+1, len(count)):
            if count[i] * count[j] > max_mult:
                if (
                    (positions[i][LEFT][col] <= positions[j][TOP][col] <= positions[i][RIGHT][col] and
                    positions[j][TOP][row] <= positions[i][LEFT][row] <= positions[j][BOTTOM][row])
                    or
                    (positions[j][LEFT][col] <= positions[i][TOP][col] <= positions[j][RIGHT][col] and
                    positions[i][TOP][row] <= positions[j][LEFT][row] <= positions[i][BOTTOM][row])
                    
                    or
                    (positions[i][LEFT][row] == positions[j][LEFT][row] and
                    positions[i][LEFT][col] <= positions[j][LEFT][col] <= positions[i][RIGHT][col])
                    or
                    (positions[i][LEFT][row] == positions[j][LEFT][row] and
                    positions[i][LEFT][col] <= positions[j][RIGHT][col] <= positions[i][RIGHT][col])
                    
                    or
                    (positions[i][TOP][col] == positions[j][TOP][col] and
                    positions[i][TOP][row] <= positions[j][TOP][row] <= positions[i][BOTTOM][row])
                    or
                    (positions[i][TOP][col] == positions[j][TOP][col] and
                    positions[i][TOP][row] <= positions[j][BOTTOM][row] <= positions[i][BOTTOM][row])
                ):
                    continue
                else:
                    max_mult = count[i] * count[j]
    
    return max_mult


if __name__ == '__main__':
    grid = [
        'GGGGGGGGGGGG',
        'GBGGBBBBBBBG',
        'GBGGBBBBBBBG',
        'GGGGGGGGGGGG',
        'GGGGGGGGGGGG',
        'GGGGGGGGGGGG',
        'GGGGGGGGGGGG',
        'GBGGBBBBBBBG',
        'GBGGBBBBBBBG',
        'GBGGBBBBBBBG',
        'GGGGGGGGGGGG',
        'GBGGBBBBBBBG'
    ]
    
    print(twoPluses(grid))
