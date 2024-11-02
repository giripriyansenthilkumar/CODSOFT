board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")

def check_winner(player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)

def minimax(is_ai):
    if check_winner("O"): return 1
    if check_winner("X"): return -1
    if " " not in board: return 0

    best_score = -2 if is_ai else 2
    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_ai else "X"
            score = minimax(not is_ai)
            board[i] = " "
            best_score = max(score, best_score) if is_ai else min(score, best_score)
    return best_score

def ai_move():
    best_score, move = -2, 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score, move = score, i
    board[move] = "O"

def human_move():
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Invalid move. Try again.")
        human_move()

while True:
    print_board()
    if check_winner("O"):
        print("AI wins!")
        break
    if check_winner("X"):
        print("You win!")
        break
    if " " not in board:
        print("It's a tie!")
        break

    human_move()
    if " " in board and not check_winner("X"):
        ai_move()