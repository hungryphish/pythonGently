'''Function shuffles a list of numbers'''
import random

def shuffle(numbers):
  #loop through the length of list, num gives us index to reference later.
  for num in range(len(numbers)):
    #the position we swap our current number with.
    swappee=(random.randrange(0,len(numbers)))
    #swappign the numbers.
    numbers[num], numbers[swappee]= numbers[swappee], numbers[num]
  return(numbers)

print(shuffle([1,2,3,4,5]))

random.seed(42)

# Perform this test ten times:

for i in range(10):

    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    shuffle(testData1)

    # Make sure the number of values hasn't changed:

    assert len(testData1) == 10

    # Make sure the order has changed:

    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Make sure that when re-sorted, all the original values are there:

    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 

# Make sure an empty list shuffled remains empty:

testData2 = []

shuffle(testData2)

assert testData2 == []
