def is_bound(i, j, grid):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid) and grid[i][j] != "X"


def minimumMoves(grid, startX, startY, goalX, goalY):
    if startX == goalX and startY == goalY:
        return 0

    visited = [[0] * len(grid) for _ in range(len(grid))]
    origins = visited.copy()
    queue = [(startX, startY, None)]
    visited[startX][startY] = True
    while queue:
        i, j, direction = queue.pop(0)
        if i == goalX and j == goalY:
            break
        
        positions = {
            "top": (i-1, j),
            "right": (i, j+1),
            "bottom": (i+1, j),
            "left": (i, j-1)
        }
        for direc, pos in positions.items():
            x,y = pos[0], pos[1]
            while is_bound(x, y, grid):
                if not visited[x][y]:
                    visited[x][y] = True
                    origins[x][y] = (i, j)
                    queue.append((x, y, direc))

                if direc == "top":
                    x -= 1
                elif direc == "right":
                    y += 1
                elif direc == "bottom":
                    x += 1
                else:
                    y -= 1

    i, j = goalX, goalY
    stack = []
    while i != startX or j != startY:
        stack.append((i,j))
        i, j = origins[i][j]

    return len(stack)
                    

if __name__ == '__main__':
    # grid = [
    #     ['.', '.', '.', '.', '.', '.', '.'],
    #     ['.', '.', '.', '.', '.', '.', '.'],
    #     ['.', '.', '.', '.', '.', '.', '.'],
    #     ['.', '.', '.', '.', '.', '.', '.'],
    #     ['.', '.', '.', '.', '.', '.', '.'],
    #     ['.', '.', '.', '.', '.', '.', '.'],
    #     ['.', '.', '.', '.', '.', '.', '.'],
    # ]
    grid = [
        ['.', '.','.', '.'],
        ['.', '.','X', 'X'],
        ['.', '.','.', '.'],
        ['.', '.','.', '.'],
    ]
    print(minimumMoves(grid, 3, 3, 0, 3))