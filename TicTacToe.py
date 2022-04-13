
board_list = [["_" for x in range(0, 3)] for i in range(0, 3)]

# Defining game mechanics functions
def board():
    print("-" * 9)
    for row in board_list:
        print(end="|")
        print(end=f" {row[0]} {row[1]} {row[2]} ")
        print(end="|\n")
    print("-" * 9)


def winner_x():
    return any(substring == ['X', 'X', 'X']
               for substring in (
                   board_list[0], board_list[1], board_list[2],
                   [i[0] for i in board_list], [i[1] for i in board_list], [i[2] for i in board_list],
                   [board_list[0][0], board_list[1][1], board_list[2][2]],
                   [board_list[0][2], board_list[1][1], board_list[2][0]]
               ))


def winner_o():
    return any(substring == ['O', 'O', 'O']
               for substring in (
                   board_list[0], board_list[1], board_list[2],
                   [i[0] for i in board_list], [i[1] for i in board_list], [i[2] for i in board_list],
                   [board_list[0][0], board_list[1][1], board_list[2][2]],
                   [board_list[0][2], board_list[1][1], board_list[2][0]]
               ))


def draw():
    for sublist in board_list:
        for i in sublist:
            if i == "_":
                return False
    if winner_o() is False and winner_x() is False:
        return True
    else:
        return False


def end_game():
    if draw():
        print("Draw")
    elif winner_o():
        print("O wins")
    elif winner_x():
        print("X wins")
    else:
        return False


def play():
    board()
    current_play = "X"
    while end_game() is False:
        # Handling user's play input
        input_2_list = input("Enter the coordinates: ").split()

        # Pre-error handling conversions
        int_list = []
        [int_list.append(int(string_input)) for string_input in input_2_list]

        # Error handling in second user input
        if isinstance(int_list[0], str) or isinstance(int_list[1], str):
            print("You should enter numbers!")
        # Adding the move to the list and the game board, or giving the user an error
        elif int_list[0] <= 3 and int_list[1] <= 3:
            if board_list[int_list[0]-1][int_list[1]-1] == "_":
                board_list[int_list[0]-1][int_list[1]-1] = current_play
                board()
                # Redefining the next play
                if current_play == "X":
                    current_play = "O"
                else:
                    current_play = "X"
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")


play()