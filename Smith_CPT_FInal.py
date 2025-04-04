#rock paper scissors game

player1 = input("Player 1, choose rock, paper, or scissors: ")
player2 = input("Player 2, choose rock, paper, or scissors: ")

if player1 == player2:
    print("It is a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
elif player1 == "paper": 
    if player2 == "rock":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")