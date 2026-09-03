#Jitender Rajpoot

def find_max(nums):     #function find max number in a list of numbers
  largest = nums[0]     #pretend first num is biggest num at index 0
  for num in nums:      #look through each number in collections nums--one at a time
    if num > largest:   #if the num I'm looking at is largest I've found
      largest = num     #make the current num new biggest num
  return largest        #give largest num

userInput = (input("Enter 5 numbers separated by spaces"))
nums = [int(x) for x in userInput.split()] #break input at spaces, turn str into int for each input part, turn into list
print(find_max(nums))      #find biggest in the nums list taken from input

