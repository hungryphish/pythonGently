'''
Sum of a 6 sided dice roll. Number of dice is user defined.
'''

import random

def rollDice(numberOfDice):
  rolls=[]
  while numberOfDice > 0:
    rolls.append(random.randint(1,6))
    numberOfDice -= 1
  return(sum(rolls))

print(rollDice(1))

assert rollDice(0) == 0

assert rollDice(1000) != rollDice(1000)

for i in range(1000):

    assert 1 <= rollDice(1) <= 6

    assert 2 <= rollDice(2) <= 12

    assert 3 <= rollDice(3) <= 18

    assert 100 <= rollDice(100) <= 600
    

'''Solution given by book'''
    
#     # Import the random module for its randint() function.

# ____ random

 

# def rollDice(numberOfDice):

#     # Start the sum total at 0:

#     total = ____

#     # Run a loop for each die that needs to be rolled:

#     for i in range(____):

#         # Add the amount from one 6-sided dice roll to the total:

#         total += random.randint(____, ____)

#     # Return the dice roll total:
