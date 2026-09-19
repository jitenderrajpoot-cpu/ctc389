#Jitender Rajpoot
#lab 8 "Final Destination" [5 decisions with 3 choices adventure game]

#get user name, global variable
userName = input("Enter your name: ")

#function to run decisons and choices

def play_game():

    print("Hi, ", userName, ". Welcome to 'Final Destination'--an interactive game in which you navigate death, I mean, navigate your way to the Moon and back to Earth. You mission is to bring something back from the Moon. Safe travels!")

#decision 1 choose vehicle
    print("Choose your spacecraft:")
    print("1. Space Shuttle")
    print("2. Solar Shuttle")
    print("3. Prototype Shuttle")

    choice1 = int(input("Enter 1, 2, or 3: "))

    if choice1 == 1:
        print("Sorry, rocket fuel prices are unaffordable. This shuttle can't fly to the Moon and back. Game over!")
    elif choice1 == 2:
        print("Great choice! Sun's fusion will power you to the Moon!")

        #decision 2 choose route
        print("Choose your flight path: ")
        print("1. Lunar Orbit")
        print("2. Fly to the Moon and back")
        print("3. Land on the Moon")

        choice2 = int(input("Enter 1, 2, or 3: "))

        if choice2 == 1:        #choice 2 = nested loop inside choice 1
            print("The shuttle remains in an infinite loop rotating around the moon. Sorry, you die due to dehydration on day 99. Game over!")
        elif choice2 == 2:
            print("You returned back to Earth but never stopped on the Moon to bring anything back.")
            print("Although you technically saw the Moon from close range, it's a failed mission. Sorry, game over!")
        elif choice2 == 3:
            print("Well done! You made it to the Moon. Now let's explore, but first let's nourish your body.")

            #decision 3 choose nourishment
            print("What do you want to eat?")
            print("1. High energy food")
            print("2. Freeze dried meal")
            print("3. Canned tuna with peppers and ailoi")

            choice3 = int(input("Enter 1, 2, or 3: "))

            if choice3 == 1:        #choice 3 = nested loop inside choice 2
                print("This food has too many calories. Unfortunately with your low blood pressure but high blood glucose level, you heart can't take the torture and decides to give up. Sorry, you die. Game over!")
            elif choice3 == 2:
                print("These items have an unsavory flavor and undesirable texture yet exactly what your body needs.")

                #decision 4 choose activity
                print("Now, let's find an activity to do. What would you like?")
                print("1. Collect Moon Rocks")
                print("2. Conduct Experiments")
                print("3. Take Photographs")

                choice4 = int(input("Enter 1, 2, or 3"))

                if choice4 == 1:     #choice 4 = nested loop inside choice 3
                    print("This was your lucky  move! You've found rare Moon Diamonds, which will pay for the next 3 generations of your family.")
                    print("You should head back to Earth and enjoy your wealth. Where do you want to land?")
                    print("1. Ocean Landing")
                    print("2. Desert Landing")
                    print("3. Landing Pad")

                    choice5 = int(input("Enter 1, 2, or 3: "))

                    if choice5 == 1:    #choice 5 = nested loop inside choice 4
                        print("You win! Ocean was the safest return path. Enjoy your Moon Diamonds! You win!!!")
                    elif choice5 == 2:
                        print("The desert ambient temperature combined with the heat generated upon your re-entry to Earth disintegrates the spacecraft.")
                        print("Everything--including the Moon Diamonds and you--vaporiize into thin air. Sorry, you die. Game over!")
                    elif choice5 == 3:
                        print("The reverse booster engines to decelerate the spacecraft malfunction and accelerate instead.")
                        print("At the sound of speed, you die with a Sonic Boom. Sorry, game over!")

                elif choice4 == 2:      #tab outside return to choice4 outside nested loop 5
                    print("The gases released from the chemical reactions are poisonous.")
                    print("Your sweat pores extract every red blood cell from your body. Sorry, you die. Game over!")
                elif choice4 == 3:
                    print("The camera batteries aren't meant to operate in the Moon's extreme temperatures. The camera explodes severing your cranial nerves.")
                    print("So, you feel no pain, but take 72 hours to  bleed out. Sorry, you die. Game over!")

            elif choice3 == 3:      #tab outside return to choice3 outside nested loop 4
                print("This was the worst choice. All items were infected with botulinum toxins.")
                print("You died a slow suffocating death from lung paralysis. Sorry, game over!")

    elif choice1== 3:                  #tab outside return to choice1
        print("The prototype wasn't tested properly. It exploded at Mach 20 speed while exiting Earth. Sorry, you die. Game over!")

#main program
play_game()             #call the function

play_again = input("Do you want to play again? Type 'yes' or 'no': ")

while play_again == 'yes':              #while loop to keep playing until player wants to stop
    play_game()
    play_again = input("Would you like to play again? ")
else:
    print("Thanks for playing 'Final Destination.' Hope you had fun. Safe travels!")



