#Jitender Rajpoot
#Python practice 1.1.1

def binarySearch(arr, x):
  l, h = 0, len(arr) - 1
  while l <= h:
    mid = (h + l) // 2
    #if element at middle
    if arr[mid] == x:
      return mid
    #if element smaller than mid
    elif arr[mid] < x:
      l = mid + 1
    #else element in left half
    else:
      h = mid - 1
  return -1

arr = [2,4,6,8,10,12,14]
x = int(input("Enter an even number"))
result = binarySearch(arr, x)
print("Result: " , result)

























