import random# importing the random module
# initializing the variables
choices = ('r', 'p', 's')
cPoints = 0
pPoints = 0

def player():
    '''This function is used to get player choice.'''
    global choices # declaring the variable choices to be global
    symbol = input("Choose either rock(r), paper(p), or scissor(s): ").lower()
    if symbol not in choices:
        print("You did not eneter a valid option. ")
        return player() # using recursion to get valid input
    else:
        return symbol # If valid input return the answer
    
def computer():
    """This function is used to get computer choice"""
    return random.choice(choices)

def game():
    '''This fucntion used to play a single round of game'''
    global cPoints, pPoints # declaring cPoints and pPoints to be global
    pChoice = player() # Getting the players choice 
    cChoice = computer() # Getting the computer chioce
    print("The computer has chosen ", cChoice)
    print("You chose ",pChoice )
    if pChoice == cChoice: # checking for tie.
        print("It's a tie! No one gets a points. ")
    elif (pChoice == 'r' and cChoice == 's') or (pChoice == 's' and cChoice == 'p') or (pChoice == 'p' and cChoice == 'r'):
        print("You won! ") 
        pPoints += 1 # increment the player point by 1
    else:
        print("Aww. I won. ")
        pPoints += 1 # increment the computer point by 1
    print()
print("Welcom to Rock Paper and Scissor game!!!")
while True: # creating an infinite loop
    for i in range(5):
        game() # Calling the game for every single time
        print("Good job!\nYour score is:", pPoints, "\nMy score is", cPoints) #displaying the result after 5 rounds
        print()

        again = int(input("Press 1 to continue\nPress2 to reset and continue\npress 3 to exit "))
        if again==1: #this is executed if the user wants to play another 5 rounds
            continue
        elif again==2: #this is executed if the user wants to reset the scores and play another 5 rounds
            pPoints=0
            cPoints=0
            continue
        else: #this is executed if the user wants to quit.
            break
     
    print("Ok! Bye!")