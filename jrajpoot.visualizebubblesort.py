#Jitender Rajpoot
#visualize bubble sort


import matplotlib.pyplot as plt   #import plot library, shortcut as plt

def bubble_sort_visualized(arr):    #function bubble sorts/visualizes, take arr as arg
  n = len(arr)                      #variable length of array
  iterations = 0
  for i in range(n):                 #for item in range of length array
    swapped = False                  #initially no swaps
    for j in range(0, n-i-1):       #for item in position to 0 to len of array-item in array-1=look at each item in array sequentially
      iterations += 1               #add 1 to iterations variable
      #print(iterations)             #print
      if arr[j] > arr[j+1]:         #if item in array>next item in array
        arr[j], arr[j+1] = arr[j+1], arr[j]   #move larger num to next position
        swapped = True                        #change swap to true
    if not swapped:                 #if nothing was swapped
      break                         #array is sorted
  return iterations              #return number of comparisons

lengths = [5,10,20,50,100]       #list with different list sizes
sortedList = [bubble_sort_visualized(list(range(i, 0, -1))) for i in lengths]
#short for loop;for i in lengths list;start at i, count down to 0, go backwards by 1
#send list to function bubble_sort_visualized
print(sortedList)       #display results

plt.plot(lengths, sortedList, marker='o')     #x-axis=lengths; y-axis=sortedList, o=circle at data point
plt.title('Iterations taken by Bubble Sort for lists of different lengths')   #provide title
plt.xlabel('List Length')                     #label x-axis
plt.ylabel('Iterations')                      #lable y-axis
plt.grid(True)                                #add grid lines to graph
plt.show()                                    #display graph

