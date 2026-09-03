#Jitender Rajpoot
#Lab7Modified ExtraCredit1: Guessing Game

def game():
    num = 7

    userGuess = int(input("Guess a number between 1 and 10: "))

    while 5 <= userGuess <= 9 and userGuess != 7:
        userGuess = int(input("Close, try again: "))

    if userGuess > 9:
        print("Sorry, you lost. Your guess was higher than my number which is 7.")

    elif userGuess < 5:
        print("Sorry, you lost. Your guess was lower than my number which is 7.")

    else:
        print("Well done! You guessed my number.")

#Main program
print("Type 'yes' or 'no'.")
userPlay = input("Would you like to play my guessing game? ")

while userPlay == "yes":
    game()
    userPlay = input("Would you like to play again: 'yes' or 'no'?  ")

if userPlay == "no":
    print("Thanks for playing. Have a blessed day!")

