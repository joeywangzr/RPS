import random

userchoice = ['R', 'P', 'S']

# Instructions for the game
print("Winning Rules of the Rock paper scissor game as follows: \n"
                            +"Rock vs paper -> paper wins \n"
                            + "Rock vs scissors -> Rock wins \n"
                            +"paper vs scissors -> scissors wins \n") 
  
# Infinite loop, will only be broken with break
while True: 
    print("Enter choice \n 1. Rock (R)\n 2. Paper (P)\n 3. Scissors (S)\n") 

# Take user input
    user = input("Pick one: ")
    user = user.upper()

    while user not in userchoice:
        user = input("Select a valid choice: ")
        user = user.upper()

    if user == "R":
        user = "Rock"
        print("User has selected: " + user)
    elif user == "S":
        user = "Scissors"
        print("User has selected: " + user)
    elif user == "P":
        user = "Paper"
        print("User has selected: " + user)

# Computer chooses
    comp = random.randint(1,3)
    if comp == 1:
        comp = 'Rock'
    if comp == 2:
        comp = 'Paper'
    else:
        comp = 'Scissors'

    print("Computer has chosen: " + comp)
    print(user + " vs " + comp)

    if comp == user:
        print("TIE")
    elif comp == 'Rock':
        if user == 'Paper':
            print("Paper beats Rock!")
            print("User wins!")
        elif user == 'Scissors':
            print("Rock beats Scissors!")
            print("User loses.")
    elif comp == 'Paper':
        if user == 'Rock':
            print("Paper beats Rock!")
            print("User loses.")
        elif user == 'Scissors':
            print("Scissors beats Paper!")
            print("User wins!")
    else:
        if user == 'Rock':
            print("Rock beats Scissors!")
            print("User wins!")
        elif user == 'Paper':
            print("Scissors beats Paper!")
            print("User loses.")
    
    again = input("Play again? y/n ")
    if again == 'n':
        print("Thanks for playing.")
        break