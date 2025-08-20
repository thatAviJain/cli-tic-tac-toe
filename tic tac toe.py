board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
# print(board)

game_still_going_on = True
current_player = 'X'
valid_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def display_board():

    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


display_board()


def switch_player():

    global current_player

    if current_player == 'X':
        current_player = 'O'

    else:
        current_player = 'X'


def check_row():

    global board, current_player, game_still_going_on
    # Row 1
    if board[0] == board[1] == board[2] != '-':
        print(f"{current_player} has won")
        game_still_going_on = False

    # Row 2
    if board[3] == board[4] == board[5] != '-':
        print(f"{current_player} has won")
        game_still_going_on = False

    # Row 3
    if board[6] == board[7] == board[8] != '-':
        print(f"{current_player} has won")
        game_still_going_on = False


def check_column():

    global board, current_player, game_still_going_on
    # Column 1
    if board[0] == board[3] == board[6] != '-':
        print(f"{current_player} has won")
        game_still_going_on = False

    # Column 2
    if board[1] == board[4] == board[7] != '-':
        print(f"{current_player} has won")
        game_still_going_on = False

    # Column 3
    if board[2] == board[5] == board[8] != '-':
        print(f"{current_player} has won")
        game_still_going_on = False


def check_diagonal():

    global board, current_player, game_still_going_on
    # Diagonal 1
    if board[0] == board[4] == board[8] != '-':
        print(f"{current_player} has won")
        game_still_going_on = False

    # Diagonal 2
    if board[2] == board[4] == board[6] != '-':
        print(f"{current_player} has won")
        game_still_going_on = False


def check_if_win():
    check_row()
    check_column()
    check_diagonal()

def check_tie():
    global game_still_going_on
    if "-" not in board and game_still_going_on:
        print("It's a tie!")
        game_still_going_on = False



while game_still_going_on:

    print(f"{current_player}'s Chance\n")

    user_input = input("Enter a space between (1 - 9): ")

    if user_input in valid_inputs:
        user_input = int(user_input)

        if board[user_input-1] == "-":

            board[user_input-1] = current_player

            display_board()
            check_if_win()
            check_tie()
            switch_player()
        else:
            print("The space is already taken up")
            continue

    else:
        print("Please check your input!")
