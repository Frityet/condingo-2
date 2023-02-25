# Write your code here!

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def checkwin(board: [[int]]) -> str:
    for row in board:
        if row[0] == row[1] == row[2] != 0:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    return None


current_player = 'X'
while True:
    for row in board:
        print(row)
    print(f"Player {current_player}'s turn")
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    board[row][col] = current_player
    current_player = 'X' if current_player == 'O' else 'O'

    winner = checkwin(board)
    if winner:
        print(f"Player {winner} wins!")
        break
