import os, sys
from subprocess import Popen
from tkinter import *
from tkinter import messagebox

from random import choice

root = Tk()
root.title("Tic Tac Toe")
root.geometry("500x520")
root.configure(bg="#fff")
root.resizable(False, False)

PLAYERS = ["O", "X"]
DEFAULT_CHARACTER = "-"
board = [[DEFAULT_CHARACTER for _ in range(3)] for _ in range(3)]
LAST_CHANCE = choice(PLAYERS)

heading = Label(root, text="Tic Tac Toe", fg="#000", bg="#fff", font=("Open Sans", 25, "bold"))
heading.place(x=150, y=7)

player = Label(root, text=f"{LAST_CHANCE}'s chance", fg="#000", bg="#fff", font=("Open Sans", 11, "bold"))
player.place(x=200, y=45)

# frame = Frame(root, height=404, width=404, bg="grey", border=0)
# frame.place(x=50, y=60)

board = [['-' for _ in range(3)] for _ in range(3)]
btns = []

def get_next_player(last=LAST_CHANCE):
    return [player for player in PLAYERS if player != last][0]

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

def takeInput(row, column):
    global LAST_CHANCE
    def on_click():
        global LAST_CHANCE
        board[row][column] = LAST_CHANCE
        btns[row][column].configure(text=LAST_CHANCE, fg="black", state=DISABLED)

        if won_by := is_win(board=board):
            re_play = messagebox.askretrycancel("Game Over", f"{won_by} WON.\n\nDo you want to retry?")
            if re_play:
                Popen([sys.executable, f"{os.getcwd()}/game.py"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
                root.destroy()
            else:
                root.destroy()
        elif not is_any_block_empty(board=board):
            re_play = messagebox.askretrycancel("Game Over", f"DRAW.\n\nDo you want to retry?")
            if re_play:
                Popen([sys.executable, f"{os.getcwd()}/game.py"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
                root.destroy()
            else:
                root.destroy()
        else:
            LAST_CHANCE = get_next_player(LAST_CHANCE)
            player['text'] = f"{LAST_CHANCE}'s chance"

    return on_click

for row in range(3):
    temp = []
    frame = Frame(root, height=int(402/3), width=404, bg="red", border=10)
    frame.place(x=50, y=65+(int(402/3))*row)
    for column in range(3):
        btn = Button(frame, text=board[row][column], bg="pink", font=("Open Sans", 55, "bold"), command=takeInput(row, column))
        btn.pack(side=LEFT, fill=BOTH, expand=1)
        temp.append(btn)
    btns.append(temp)

root.mainloop()