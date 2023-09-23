def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(board, player):
    return ((board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player))

def play():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = "X"
    while True:
        print_board(board)
        move = input("Player " + current_player + ", enter your move (1-9): ")
        move = int(move) - 1
        if board[move] != "X" and board[move] != "O":
            board[move] = current_player
            if check_win(board, current_player):
                print_board(board)
                print("Congratulations, player " + current_player + " wins!")
                break
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        else:
            print("That space is already taken. Please choose another move.")

play()