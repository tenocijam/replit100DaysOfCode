# Day 17

from getpass import getpass as input

print()
print("Welcome to the Rock Paper Scissors battleground")
print()

roundNumber = 1
player1Score = 0
player2Score = 0

while True:
    print()
    print("Round", roundNumber)
    print("Select your move: ")
    player1 = input("Player 1 (R, P, S): ")
    player2 = input("Player 2 (R, P, S): ")
    winner = -1
    
    if player1 == "R":
        player1Move = "Rock"
        if player2 == "R":
            winner = 0
        elif player2 == "P":
            winner = 2
        elif player2 == "S":
            winner = 1
    elif player1 == "P":
        player1Move = "Paper"
        if player2 == "R":
            winner = 1
        elif player2 == "P":
            winner = 0
        elif player2 == "S":
            winner = 2
    elif player1 == "S":
        player1Move = "Scissor"
        if player2 == "R":
            winner = 2
        elif player2 == "P":
            winner = 1
        elif player2 == "S":
            winner = 0
    
    # Converting player2 moves into full move names   
    if player2 == "R":
        player2Move = "Rock"
    elif player2 == "P":
        player2Move = "Paper"
    elif player2 == "S":
        player2Move = "Scissor"
    
    print()
    
    if winner == 0:
        print("It's a draw! No points awarded.")
    elif winner == 1:
        print("Player 1's", player1Move, "destroyed", "player 2's", player2Move)
        player1Score += 1
    elif winner == 2:
        print("Player 2's", player2Move, "destroyed", "player 1's", player1Move)
        player2Score += 1
    else:
        print("Invalid input. Please try again.")

    roundNumber += 1

    if player1Score == 3:
        print("Player 1 scored 3 points and won the game")
        print("Player 2 score:", player2Score)
        exit()
    elif player2Score == 3:
        print("Player 2 scored 3 points and won the game")
        print("Player 1 score:", player1Score)
        exit()