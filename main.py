from random import choice

PLAYERS = ["O", "X"]
DEFAULT_CHARACTER = "-"
board = [[DEFAULT_CHARACTER for _ in range(3)] for _ in range(3)]
LAST_CHANCE = choice(PLAYERS)

def display_board(board=board):
    for row in board:
        for block in row:
            print(block, end="\t")
        print()
    print()

def chance(user, board=board):
    while True:
        row, column = eval(input("Enter the your desired position in the format (x, y) where is the row number and y is the column number: "))
        if row-1 > 3 or column-1 > 3:
            print("Invalid Choice.")
            continue
        elif board[row-1][column-1] != DEFAULT_CHARACTER:
            print("Position isn't empty.")
            continue
        else:
            board[row-1][column-1] = user
            break

    return print()

def is_win(board=board):
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != DEFAULT_CHARACTER:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != DEFAULT_CHARACTER:
        return board[0][2]

    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != DEFAULT_CHARACTER:
            return board[row][0]

    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != DEFAULT_CHARACTER:
            return board[0][column]

    return None

def is_any_block_empty(board=board):
    for row in board:
        for block in row:
            if block == DEFAULT_CHARACTER:
                return True
    else:
        return False

def get_next_player(last=LAST_CHANCE):
    return [player for player in PLAYERS if player != last][0]

while is_any_block_empty(board):
    display_board(board)
    print(f"{LAST_CHANCE}'s Chance.")
    chance(LAST_CHANCE, board)
    if is_win(board):
        display_board(board)
        print(f"{is_win(board)} Won.")
        break
    LAST_CHANCE = get_next_player(LAST_CHANCE)
else:
    print("Match Draw.")