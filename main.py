view = """\
1 {a[0][0]} │ {a[0][1]} │ {a[0][2]}
  ──┼───┼──
2 {a[1][0]} │ {a[1][1]} │ {a[1][2]}
  ──┼───┼──
3 {a[2][0]} │ {a[2][1]} │ {a[2][2]}
  a   b   c\
"""

board = [3 * [' '] for i in range(3)]

# Returns 0 if nobody wins, 1 if X wins, 2 if O wins
def winner():
    # Check cols
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return True
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[2][1] == board[1][1] == board[0][2]:
        return True
    return False

nmoves = 0
while True:
    # make a move X

    # if win, exit X WIN
    # if nmoves = 9, exit DRAWi
    # make a move 
    # if win, exit Y WIN

