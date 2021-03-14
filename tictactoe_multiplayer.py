TheBoard = {'1':' ', '2':' ', '3':' ',
            '4':' ', '5':' ', '6':' ',
            '7':' ', '8':' ', '9':' '}

board_keys = []

for key in TheBoard:
    board_keys.append(key)

turn = [0]

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


def try_again(winner):
    turn[0] +=1
    if turn[0] %2 == 1:
        if winner == players[0]:
            score[0] += 1
        elif winner == players[1]:
            score[1] += 1
        print("The score for {} is {}".format(p1, score[0]))
        print("The score for {} is {}".format(p2, score[1]))
    else:
        if winner == players[0]:
            score[1] += 1
        elif winner == players[1]:
            score[0] += 1
        print("The score for {} is {}".format(p1, score[0]))
        print("The score for {} is {}".format(p2, score[1]))

    play_again = input("Do you want to play again?\n")
    if play_again == "yes" or play_again == "y":
        for key in board_keys:
            TheBoard[key] = " "

        print(f"Restarting the game, now {players[1]} will play first.")
        temp = players[0]
        players[0] = players[1]
        players[1] = temp

        tictactoe()
    else:
        exit(0)


def win_check(player):

    if TheBoard["1"] == TheBoard["2"] == TheBoard["3"] != " ":
        print(f"{player} has won!")
        try_again(player)
    elif TheBoard["4"] == TheBoard["5"] == TheBoard["6"] != " ":
        print(f"{player} has won!")
        try_again(player)
    elif TheBoard["7"] == TheBoard["8"] == TheBoard["9"] != " ":
        print(f"{player} has won!")
        try_again(player)
    elif TheBoard["1"] == TheBoard["4"] == TheBoard["7"] != " ":
        print(f"{player} has won!")
        try_again(player)
    elif TheBoard["2"] == TheBoard["5"] == TheBoard["8"] != " ":
        print(f"{player} has won!")
        try_again(player)
    elif TheBoard["3"] == TheBoard["6"] == TheBoard["9"] != " ":
        print(f"{player} has won!")
        try_again(player)
    elif TheBoard["1"] == TheBoard["5"] == TheBoard["9"] != " ":
        print(f"{player} has won!")
        try_again(player)
    elif TheBoard["3"] == TheBoard["5"] == TheBoard["7"] != " ":
        print(f"{player} has won!")
        try_again(player)

def tictactoe():
    print_board(TheBoard)
    i = 0
    while i < 5:
        invalid = False

        while not invalid:
            print("Make your move ", players[0])
            move = input()
            if TheBoard[move] == " ":
                if turn[0] % 2 == 0:
                    TheBoard[move] = X
                else:
                    TheBoard[move] = O
                print_board(TheBoard)
                win_check(players[0])
                invalid = True

            else:
                print("Invalid move.")

        invalid = False

        if i != 4:
            while not invalid:
                print("Make your move", players[1])
                move = input()
                if TheBoard[move] == " ":
                    if turn[0] % 2 == 0:
                        TheBoard[move] = O
                    else:
                        TheBoard[move] = X
                    print_board(TheBoard)
                    invalid = True
                    win_check(players[1])
                else:
                    print("Invalid move.")

        i += 1
    if i == 5:
        print("It's a tie!")
        try_again(0)



print("Please insert you names.")

p1 = input("Player 1: ")
p2 = input("Player 2: ")
players = [p1, p2]

print("Do you want X or O?")

X = input(p1 + ": ")
O = input(p2 + ": ")

score1 = 0
score2 = 0
score = [score1, score2]

tictactoe()
