#Jitender Rajpoot
#factorialFunction

def factorial(n):       #function called 'factorial'; n is num user can input later
  return 1 if n == 0 else n * factorial(n-1)    #multiply num by all positive nums below it
                                            #if n=0 return 1=base case tell function to stop
                                            #otherwise multiple n with n-1 until 0 is reached
userInput = int(input("Enter a number: "))
outputMsg = factorial(userInput)
print(outputMsg)
