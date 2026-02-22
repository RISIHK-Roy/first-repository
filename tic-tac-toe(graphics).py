import tkinter as tk
import random

# game state
board = [" "] * 9
current_player = "X"

# ---------- game logic ----------
def win(player):
    win_combo = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_combo:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def computer_move():
    empty_spots = [i for i in range(9) if board[i] == " "]
    return random.choice(empty_spots)

# ---------- GUI logic ----------
def handle_click(index):
    global current_player

    if board[index] != " ":
        return

    board[index] = "X"
    buttons[index].config(text="X", state="disabled")

    if win("X"):
        status_label.config(text="Player X wins!")
        disable_all()
        return

    if " " not in board:
        status_label.config(text="It's a draw!")
        return

    # computer move
    move = computer_move()
    board[move] = "O"
    buttons[move].config(text="O", state="disabled")

    if win("O"):
        status_label.config(text="Computer wins!")
        disable_all()

def disable_all():
    for btn in buttons:
        btn.config(state="disabled")

# ---------- Tkinter setup ----------
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []

for i in range(9):
    btn = tk.Button(
        root,
        text=" ",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: handle_click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status_label = tk.Label(root, text="Your turn (X)", font=("Arial", 14))
status_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
