class Checker:
    
    def __init__(self, row, col, rowIncrement, colIncrement):
        self.row = row
        self.col = col
        self.rowIncrement = rowIncrement
        self.colIncrement = colIncrement

    def increment(self):
        self.row += self.rowIncrement
        self.col += self.colIncrement

    def in_bound(self, size) -> bool:
        return self.row >= 0 and self.row < size and self.col >= 0 and self.col < size


def to_check(checker: Checker, board):
    first = board[checker.row][checker.col]
    while checker.in_bound(len(board)):
        value = board[checker.row][checker.col]
        if value != first:
            return -1
        else:
            checker.increment()
    
    return first  # winner



def get_won(board):
    lines_to_check = []
    for i in range(len(board)):
        lines_to_check.append(Checker(i, 0, 1, 0))
        lines_to_check.append(Checker(0, i, 0, 1))
    
    lines_to_check.append(Checker(0, 0, 1, 1))
    lines_to_check.append(Checker(0, len(board)-1, 1, -1))

    for line in lines_to_check:
        value = to_check(line, board)
        if value != -1:
            return value  # winner

    return -1


if __name__ == "__main__":
    board = [
        [1,1,1],
        [0,1,0],
        [0,0,0]
    ]
    print(get_won(board))
