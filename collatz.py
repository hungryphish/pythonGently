'''function provides the collatz list of a given number'''
def collatz(number):
  czList=[number]
  #Check if number is less than 1 if so, return empty
  if number < 1:
    return([])
  #Since 1 is the end of a sequence, we want to iterate until we get to it.
  while number != 1:
    if number % 2 ==0:
      number = number//2
      czList.append(number)
    elif number % 2 > 0:
      number = 3*number + 1
      czList.append(number)
  return(czList)
  
  

print(collatz(26))

assert collatz(0) == []

assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]

assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]

assert len(collatz(256)) == 9

assert len(collatz(257)) == 123

import random

random.seed(42)

for i in range(1000):

    startingNum = random.randint(1, 10000)

    seq = collatz(startingNum)

    assert seq[0] == startingNum # Make sure it includes the starting number.

    assert seq[-1] == 1  # Make sure the last integer is 1.
