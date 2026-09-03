#Jitender Rajpoot
#Sorting Algorithm

def quicksort(arr):     #function sorts lists 'arr'= argument
  if len(arr) <= 1:     #check if list needs sorting
    return arr          #return sorted list

  pivot = arr[len(arr) // 2]      #middle item = pivot
  left = [x for x in arr if x < pivot]    #smaller items on left
  middle = [x for x in arr if x == pivot] #equal items in middle
  right = [x for x in arr if x > pivot]   #larger items right

  return quicksort(left) + middle + quicksort(right)  #sort both sides then combine

userInput = input("Enter 5 numbers separated by spaces: ")
nums = [int(x) for x in userInput.split()]  #split userInput, turn str to int, make nums to list

print(quicksort(nums))
