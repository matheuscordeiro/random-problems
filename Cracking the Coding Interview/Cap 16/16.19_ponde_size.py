def pond_size(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    register = [[False] * cols for _ in range(rows)]
    pods = []

    for i in range(rows):
        for j in range(cols):
            if is_water(i, j, matrix) and not register[i][j]:
                pods.append(count_pond(i, j, matrix, register))

    return pods


def count_pond(i, j, matrix, register):
    total = 1
    register[i][j] = True
    height = len(matrix)
    width = len(matrix[0])

    # top
    if is_bound(i-1, j, height, width) and not register[i-1][j] and is_water(i-1, j, matrix):
        total += count_pond(i-1, j, matrix, register)

    # diagonal right top
    if is_bound(i-1, j+1, height, width) and not register[i-1][j+1] and is_water(i-1, j+1, matrix):
        total += count_pond(i-1, j+1, matrix, register)

    # right
    if is_bound(i, j+1, height, width) and not register[i][j+1] and is_water(i, j+1, matrix):
        total += count_pond(i, j+1, matrix, register)

    # diagonal right bottom
    if is_bound(i+1, j+1, height, width) and not register[i+1][j+1] and is_water(i+1, j+1, matrix):
        total += count_pond(i+1, j+1, matrix, register)

    # bottom
    if is_bound(i+1, j, height, width) and not register[i+1][j] and is_water(i+1, j, matrix):
        total += count_pond(i+1, j, matrix, register)

    # diagonal left bottom
    if is_bound(i+1, j-1, height, width) and not register[i+1][j-1] and is_water(i+1, j-1, matrix):
        total += count_pond(i+1, j-1, matrix, register)

    # left
    if is_bound(i, j-1, height, width) and not register[i][j-1] and is_water(i, j-1, matrix):
        total += count_pond(i, j-1, matrix, register)

    # diagonal top left
    if is_bound(i-1, j-1, height, width) and not register[i-1][j-1] and is_water(i-1, j-1, matrix):
        total += count_pond(i-1, j-1, matrix, register)
    
    return total


def is_bound(i, j, height, width):
    return i >= 0 and j >= 0 and i < height and j < width

def is_water(i, j, matrix):
    return matrix[i][j] == 0


if __name__ == "__main__":
    matrix = [
        [0,2,1,0],
        [0,1,0,1],
        [1,1,0,1],
        [0,1,0,1]
    ]
    print(pond_size(matrix))