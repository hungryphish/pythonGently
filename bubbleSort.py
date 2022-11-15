'''Bubble Sort Algorithim'''
def bubbleSort(numbers):
  # Variable "count" counts how many times the algorithim runs without swapping. If a swap is made, counter is reset.
  # The while loop continues until it can loop through the whole list without swapping.
  count=0
  while count < len(numbers)-1:
    for inum in range(len(numbers)):
      #To make the bubble stop at the end, else it will cause an error as last index +1 doesn't exist.
      if (inum+1) < len(numbers):
        #Test which number is larger
        if numbers[inum] > numbers[(inum+1)]:
          #swaps numbers
          numbers[inum], numbers[(inum+1)] = numbers[(inum+1)], numbers[inum]
          count=0
          # No swap needed, add 1 to the counter.
        else:
          count+=1
  return(numbers)
  
print(bubbleSort([12,18,3,4,5,9,12,15]))

assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]

assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]
