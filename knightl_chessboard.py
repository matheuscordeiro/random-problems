
# KnightL on a Chessboard
# Difficulty: Medium

def knightlOnAChessboard(n):
    board = []
    cache = [[0] * n for _ in range(n)]
    for i in range(1, n):
        row = []
        for j in range(1, n):
            if cache[i][j]:
                row.append(cache[i][j])
            else:
                movements = move(i, j, n)
                cache[i][j] = cache[j][i] = movements
                row.append(movements)

        board.append(row)

    return board


def move(a, b, n):
    depth = 0
    queue = [(0, 0, depth)]
    visited = [[False] * n for _ in range(n)]
    while queue:
        i, j, depth = queue.pop(0)
        if i == n-1 and j == n-1:
            return depth 
        
        positions = [
            (i+a, j+b), 
            (i+a, j-b),
            (i-a, j+b),
            (i-a, j-b),
            (i+b, j+a),
            (i+b, j-a),
            (i-b, j+a),
            (i-b, j-a)
        ]
        for x, y in positions:
            if is_bound(x, y, n) and not visited[x][y]:
                visited[x][y] = True
                queue.append((x, y, depth + 1))

    return -1


def is_bound(i, j, n):
    return i >=  0 and j >= 0 and i < n and j < n


if __name__ == "__main__":
    print(knightlOnAChessboard(17))
