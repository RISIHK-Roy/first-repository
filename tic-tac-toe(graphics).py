import tkinter as tk
import random

root = tk.Tk()
root.title("Tic Tac Toe")

board = [""] * 9
buttons = []
game_over = False

#checking winner..
def check_winner(player):
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def check_draw():
    return "" not in board


#computer's turn....

def computer_turn():
    global game_over

    empty = [i for i in range(9) if board[i] == ""]
    if not empty:
        return

    move = random.choice(empty)
    board[move] = "O"
    buttons[move].config(text="O", state="disabled")

    if check_winner("O"):
        status_label.config(text="Computer wins!")
        game_over = True
        disable_all()
    elif check_draw():
        status_label.config(text="It's a draw!")
        game_over = True


def player_click(index):
    global game_over

    if board[index] != "" or game_over:
        return

    board[index] = "X"
    buttons[index].config(text="X", state="disabled")

    if check_winner("X"):
        status_label.config(text="You win!")
        game_over = True
        disable_all()
        return

    if check_draw():
        status_label.config(text="It's a draw!")
        game_over = True
        return

    computer_turn()


def disable_all():
    for btn in buttons:
        btn.config(state="disabled")



def restart_game():
    global board, game_over
    board = [""] * 9
    game_over = False

    for btn in buttons:
        btn.config(text="", state="normal")

    status_label.config(text="Your turn (X)")



for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: player_click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status_label = tk.Label(root, text="Your turn (X)", font=("Arial", 14))
status_label.grid(row=3, column=0, columnspan=3)

restart_btn = tk.Button(root, text="Restart", font=("Arial", 12), command=restart_game)
restart_btn.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
