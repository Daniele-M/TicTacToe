import random

TheBoard = {'1':' ', '2':' ', '3':' ',
            '4':' ', '5':' ', '6':' ',
            '7':' ', '8':' ', '9':' '}

cross = ["1", "3", "5", "7", "9"] #contans the corner and center boxes
plus = ["2", "4", "6", "8"]

move = 0   #initialize a variable move that will later be assigned to the move of the player
           #initializing it covers the case in which the computer goes first

player = "You"
PC = "Computer"

score_board = [0, 0]
turn = [0]


# prints the updated board
def print_board(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board["1"], board["2"], board["3"]))
    print("\t_____|_____|____")

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board["4"], board["5"], board["6"]))
    print("\t_____|_____|____")

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board["7"], board["8"], board["9"]))
    print("\t     |     |")
    print("\n")



def clear_board():
    for i in TheBoard:
        TheBoard[i] = " "



def swap_turn():
    turn[0] += 1
    clear_board()
    tic_tac_toe(turn)



def score(winner):
    if winner == "You":
        score_board[0] += 1
    else:
        score_board[1] += 1

    print(f"Score = {score_board}")


# Updates the score, swaps the first and second player and starts a new game
def try_again(winner):

    if winner != 0:
        print(f"{winner} won!\nDo you want to play another game?")
        score(winner)

        play_again = input("Press y to play again, n to stop.\n")
        if "y" in play_again or "yes" in play_again:
            swap_turn()
        else:
            exit(0)
    else:
        print("It's a tie!\nDo you want to play again?")
        print(f"Score = {score_board}")

        play_again = input("Press y to play again, n to stop.\n")
        if "y" in play_again or "yes" in play_again:
            swap_turn()
        else:
            exit(0)


#Check is the game is over without a winner
def check_tie():
    if " " in TheBoard.values():
        pass
    else:
        try_again(0)



# Checks if the game is over and calls the try_again function on the winner
def check_win(player):

    if TheBoard["1"] == TheBoard["2"] == TheBoard["3"] != " ":
        try_again(player)
    elif TheBoard["4"] == TheBoard["5"] == TheBoard["6"] != " ":
        try_again(player)
    elif TheBoard["7"] == TheBoard["8"] == TheBoard["9"] != " ":
        try_again(player)
    elif TheBoard["1"] == TheBoard["4"] == TheBoard["7"] != " ":
        try_again(player)
    elif TheBoard["2"] == TheBoard["5"] == TheBoard["8"] != " ":
        try_again(player)
    elif TheBoard["3"] == TheBoard["6"] == TheBoard["9"] != " ":
        try_again(player)
    elif TheBoard["1"] == TheBoard["5"] == TheBoard["9"] != " ":
        try_again(player)
    elif TheBoard["3"] == TheBoard["5"] == TheBoard["7"] != " ":
        try_again(player)


def valid_move(p_move):

    if TheBoard[p_move] == " ":
        return 1
    else:
        return 0



# Puts the possible moves in a list
def get_emptycells():

    cells = []
    for i in TheBoard:
        if TheBoard[i] == " ":
            cells.append(i)
    return cells


# Checks if there is a possible tris, returning the right boxes, or 0 otherwise.
def check_tris(X):

    if TheBoard["1"] == " ":
        if TheBoard["2"] == TheBoard["3"] == X:
            return "1"
        elif TheBoard["4"] == TheBoard["7"] == X:
            return "1"
        elif TheBoard["5"] == TheBoard["9"] == X:
            return "1"

    if TheBoard["2"] == " ":
        if TheBoard["5"] == TheBoard["8"] == X:
            return "2"
        elif TheBoard["1"] == TheBoard["3"] == X:
            return "2"

    if TheBoard["3"] == " ":
        if TheBoard["1"] == TheBoard["2"] == X:
            return "3"
        elif TheBoard["6"] == TheBoard["9"] == X:
            return "3"
        elif TheBoard["5"] == TheBoard["7"] == X:
            return "3"

    if TheBoard["4"] == " ":
        if TheBoard["1"] == TheBoard["7"] == X:
            return "4"
        elif TheBoard["5"] == TheBoard["6"] == X:
            return "4"

    if TheBoard["5"] == " ":
        if TheBoard["1"] == TheBoard["9"] == X:
            return "5"
        elif TheBoard["3"] == TheBoard["7"] == X:
            return "5"
        elif TheBoard["2"] == TheBoard["8"] == X:
            return "5"
        elif TheBoard["4"] == TheBoard["6"] == X:
            return "5"

    if TheBoard["6"] == " ":
        if TheBoard["3"] == TheBoard["9"] == X:
            return "6"
        elif TheBoard["4"] == TheBoard["5"] == X:
            return "6"

    if TheBoard["7"] == " ":
        if TheBoard["1"] == TheBoard["4"] == X:
            return "7"
        elif TheBoard["8"] == TheBoard["9"] == X:
            return "7"
        elif TheBoard["5"] == TheBoard["3"] == X:
            return "7"

    if TheBoard["8"] == " ":
        if TheBoard["7"] == TheBoard["9"] == X:
            return "8"
        elif TheBoard["2"] == TheBoard["5"] == X:
            return "8"

    if TheBoard["9"] == " ":
        if TheBoard["7"] == TheBoard["8"] == X:
            return "9"
        elif TheBoard["3"] == TheBoard["6"] == X:
            return "9"
        elif TheBoard["1"] == TheBoard["5"] == X:
            return "9"

    return 0



def pass_move(player, move):

    check_win(player)
    check_tie()

    if player == "computer":
        player_move()
    else:
        PC_move(move)




# To take the input of the player every move and pass it to the PC moves
def player_move():

    print("It's your turn, make your move.\n")
    p_move = input()

    if valid_move(p_move) == 1:
        TheBoard[p_move] = XO
        print_board(TheBoard)

    else:
        print("Invalid move")
        player_move()

    pass_move("player", p_move)




def PC_move(move):

    if move == 0:                                #computer goes first
        TheBoard[(random.choice(cross))] = OX
        print_board(TheBoard)
        pass_move("computer", 0)
    else:

        win_move = check_tris(OX)
        obliged_move = check_tris(XO)

        if win_move != 0:
            TheBoard[win_move] = OX
            print_board(TheBoard)
            try_again("PC")

        elif obliged_move != 0:
            TheBoard[obliged_move] = OX
            print_board(TheBoard)
            pass_move("computer", 0)

        else:

            AI_brain(move)
            print_board(TheBoard)

            pass_move("computer", 0)


# Decides the move for the computer if not obvious
def AI_brain(move):

    empty_cells = get_emptycells()

    if len(empty_cells) == 8:                           # First move after the player
        if TheBoard["5"] == " ":
            TheBoard["5"] = OX
        else:
            z = set(empty_cells) - set(plus)
            temp_list = []
            for i in z:
                temp_list.append(i)
            TheBoard[random.choice(temp_list)] = OX     #The computer makes his first move in one of the cross cells

    elif len(empty_cells) == 7:                          #Second move after playing the first one

        if "5" in empty_cells:                           #In this case the computer always wins

            if move in cross:

                if TheBoard["9"] == OX:
                    if TheBoard["1"] == " ":
                        TheBoard["1"] = OX
                    else:
                        TheBoard[random.choice(["7", "3"])] = OX
                if TheBoard["1"] == OX:
                    if TheBoard["9"] == " ":
                        TheBoard["9"] = OX
                    else:
                        TheBoard[random.choice(["7", "3"])] = OX
                if TheBoard["3"] == OX:
                    if TheBoard["7"] == " ":
                        TheBoard["7"] = OX
                    else:
                        TheBoard[random.choice(["1", "9"])] = OX
                if TheBoard["7"] == OX:
                    if TheBoard["3"] == " ":
                        TheBoard["3"] = OX
                    else:
                        TheBoard[random.choice(["1", "9"])] = OX

            else:                                                   #Player played in plus
                TheBoard["5"] = OX

        elif TheBoard["5"] == OX:                                   #Computer played center
            if move in plus:
                if move == "8" or move == "2":
                    TheBoard[random.choice(["4", "6"])] = OX
                else:
                    TheBoard[random.choice(["2", "8"])] = OX        #REMEMBER LEN 5. THE COMPUTER DOES NOT ALWAYS WIN HERE

            else:                                                   #Player played cross
                cross_moves = list(set(empty_cells) & set(cross))
                TheBoard[random.choice(cross_moves)] = OX

        else:                                                       #Player played center
            if TheBoard["1"] == OX:
                TheBoard[random.choice(["3", "7"])] = OX
            elif TheBoard["3"] == OX:
                TheBoard[random.choice(["1", "9"])] = OX
            elif TheBoard["7"] == OX:
                TheBoard[random.choice(["1", "9"])] = OX
            elif TheBoard["9"] == OX:
                TheBoard[random.choice(["3", "7"])] = OX

    elif len(empty_cells) == 5:

        sett = set(empty_cells) & {"1", "3", "7", "9"}

        if sett == {"1", "3", "7", "9"}:

            if TheBoard["2"] == OX:
                TheBoard[random.choice(["1", "3"])] = OX

            if TheBoard["4"] == OX:
                TheBoard[random.choice(["1", "7"])] = OX

            if TheBoard["6"] == OX:
                TheBoard[random.choice(["3", "9"])] = OX

            if TheBoard["8"] == OX:
                TheBoard[random.choice(["7", "9"])] = OX

        else:

            if TheBoard["1"] == OX:
                if TheBoard["2"] == " ":
                    TheBoard["2"] = OX
                else:
                     TheBoard["4"] = OX

            if TheBoard["3"] == OX:
                if TheBoard["2"] == " ":
                    TheBoard["2"] = OX
                else:
                     TheBoard["6"] = OX

            if TheBoard["7"] == OX:
                if TheBoard["8"] == " ":
                    TheBoard["8"] = OX
                else:
                     TheBoard["4"] = OX

            if TheBoard["9"] == OX:
                if TheBoard["6"] == " ":
                    TheBoard["6"] = OX
                else:
                     TheBoard["8"] = OX

    else:
        TheBoard[random.choice(empty_cells)] = OX



def tic_tac_toe(turn):

    print_board(TheBoard)

    if turn[0] % 2 == 0:
        player_move()
    else:
        PC_move(0)






XO = "X"
OX = "O"

first = input("\tWho goes first?\n\t(Press 1 for player, 2 for the computer)\n")
if first == "2":
    turn[0] = 1
tic_tac_toe(turn)
