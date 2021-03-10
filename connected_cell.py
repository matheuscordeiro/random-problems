# Connected Cells in a Grid
# Difficulty: Medium

def count_filled(matrix, i, j, marked):
    if not matrix[i][j] or marked.get(f'{i}{j}'):
        return 0

    filled = 1
    marked[f'{i}{j}'] = True
    # left
    if j-1 >= 0 and not marked.get(f'{i}{j-1}') and matrix[i][j-1]:
        filled += count_filled(matrix, i, j-1, marked)

    # diagonal left top
    if j-1 >= 0 and i-1 > 0 and not marked.get(f'{i-1}{j-1}') and matrix[i-1][j-1]:
        filled += count_filled(matrix, i-1, j-1, marked)

    # top
    if i-1 > 0 and not marked.get(f'{i-1}{j}') and matrix[i-1][j]:
        filled += count_filled(matrix, i-1, j, marked)

    # diagonal top right
    if j+1 < len(matrix[0]) and i-1 > 0 and not marked.get(f'{i-1}{j+1}') and matrix[i-1][j+1]:
        filled += count_filled(matrix, i-1, j+1, marked)

    # right
    if j+1 < len(matrix[0]) and not marked.get(f'{i}{j+1}') and matrix[i][j+1]:
        filled += count_filled(matrix, i, j+1, marked)

    # diagonal right bottom
    if j+1 < len(matrix[0]) and i+1 < len(matrix) and not marked.get(f'{i+1}{j+1}') and matrix[i+1][j+1]:
        filled += count_filled(matrix, i+1, j+1, marked)

    # bottom
    if i+1 < len(matrix) and not marked.get(f'{i+1}{j}') and matrix[i+1][j]:
        filled += count_filled(matrix, i+1, j, marked)

    # diagonal left bottom
    if j-1 >= 0 and i+1 < len(matrix) and not marked.get(f'{i+1}{j-1}') and matrix[i+1][j-1]:
        filled += count_filled(matrix, i+1, j-1, marked)

    return filled


def connectedCell(matrix):
    marked = {}
    max_filled = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            aux = count_filled(matrix, i, j, marked)
            max_filled = max(aux, max_filled)
    
    return max_filled


if __name__ == '__main__':
    matrix = [
        [1,1,0],
        [1,0,0],
        [0,0,1,0],
        [0,0,1]
    ]
    print(connectedCell(matrix))