#Jitender Rajpoot Count Vowels

#Ask the user for a word.
# count = 0
word = input("Enter a word: ")  #get user to enter word

#Count how many vowels it contains.
def countVowels(word):         #function takes word/user input as argument
  count = 0			#use empty variable to keep count
  for i in word:		#for loop to cycle through input
    if (i == 'a') or (i == 'e') or (i == 'i') or (i == 'o') or (i == 'u'):
      count += 1		#add 1 to count if clause is met
  return count			#return count=tracks num of vowels
output = countVowels(word)	#vowel stores count for print statement
print('The word "',word,'" has ', output, 'vowels')

