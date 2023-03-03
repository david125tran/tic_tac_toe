
s =[" ", " ", " ", " ", " ", " ", " ", " ", " "]

print("Welcome to Tic Tac Toe")
print("Player 1 will be 'X'")
print("Player 2 will be 'O'")
print("To make a choice, type the letter followed by the number, such as 'A2'")

users_turn = [1, 2, 1, 2, 1, 2, 1, 2, 1] # Store the players' turns in a list

for turn in users_turn:
    board = "" \
            "\n  1   2   3 " \
            f"\nA {s[0]} | {s[1]} | {s[2]} " \
            "\n ---|---|---" \
            f"\nB {s[3]} | {s[4]} | {s[5]} " \
            "\n ---|---|---" \
            f"\nC {s[6]} | {s[7]} | {s[8]} "

    # Load the board
    print(board)

    # Check to see if Player 1 has won:
    if s[0] == "X":
        if s[1] == "X":
            if s[2] == "X":
                print("Player 1 wins!")
                break
    elif s[3] == "X":
        if s[4] == "X":
            if s[5] == "X":
                print("Player 1 wins!")
                break
    elif s[6] == "X":
        if s[7] == "X":
            if s[8] == "X":
                print("Player 1 wins!")
                break
    elif s[0] == "X":
        if s[3] == "X":
            if s[6] == "X":
                print("Player 1 wins!")
                break
    elif s[1] == "X":
        if s[4] == "X":
            if s[7] == "X":
                print("Player 1 wins!")
                break
    elif s[2] == "X":
        if s[5] == "X":
            if s[9] == "X":
                print("Player 1 wins!")
                break
    elif s[0] == "X":
        if s[4] == "X":
            if s[8] == "X":
                print("Player 1 wins!")
                break
    elif s[6] == "X":
        if s[4] == "X":
            if s[2] == "X":
                print("Player 1 wins!")
                break
    else:
        pass

    # Check to see if Player 2 has won:
    if s[0] == "O":
        if s[1] == "O":
            if s[2] == "O":
                print("Player 2 wins!")
                break
    elif s[3] == "O":
        if s[4] == "O":
            if s[5] == "O":
                print("Player 2 wins!")
                break
    elif s[6] == "O":
        if s[7] == "O":
            if s[8] == "O":
                print("Player 2 wins!")
                break
    elif s[0] == "O":
        if s[3] == "O":
            if s[6] == "O":
                print("Player 2 wins!")
                break
    elif s[1] == "O":
        if s[4] == "O":
            if s[7] == "O":
                print("Player 2 wins!")
                break
    elif s[2] == "O":
        if s[5] == "O":
            if s[9] == "O":
                print("Player 2 wins!")
                break
    elif s[0] == "O":
        if s[4] == "O":
            if s[8] == "O":
                print("Player 2 wins!")
                break
    elif s[6] == "O":
        if s[4] == "O":
            if s[2] == "O":
                print("Player 2 wins!")
                break
    else:
        pass

    print(" ")
    print(f"It is {turn}'s turn")

    # Make a selection that has not been chosen yet:
    while True:
        selection = input("Make your choice: ").upper()
        if selection == "A1":
            if s[0] == " ":
                break
        elif selection == "A2":
            if s[1] == " ":
                break
        elif selection == "A3":
            if s[2] == " ":
                break
        elif selection == "B1":
            if s[3] == " ":
                break
        elif selection == "B2":
            if s[4] == " ":
                break
        elif selection == "B3":
            if s[5] == " ":
                break
        elif selection == "C1":
            if s[6] == " ":
                break
        elif selection == "C2":
            if s[7] == " ":
                break
        elif selection == "C3":
            if s[8] == " ":
                break
        print("\nThis is not a valid choice, TRY AGAIN!")

    # Determine the mark:
    if turn == 1:
        mark = "X"
    elif turn == 2:
        mark = "O"

    # Make the mark on the board:
    if selection == "A1":
        s[0] = mark
    elif selection == "A2":
        s[1] = mark
    elif selection == "A3":
        s[2] = mark
    elif selection == "B1":
        s[3] = mark
    elif selection == "B2":
        s[4] = mark
    elif selection == "B3":
        s[5] = mark
    elif selection == "C1":
        s[6] = mark
    elif selection == "C2":
        s[7] = mark
    elif selection == "C3":
        s[8] = mark


print("Game Over!")
