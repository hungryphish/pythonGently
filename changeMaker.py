import math

def makeChange(money):
  #blank dictionary which is appended to throughout function and is my answer.
  change=dict()
  #each if statement subtracts from money. We want to loop while money >0
  #we round throughout because python math sucks
  while round(money) > 0:
    
    if money >= 25:
      #add quarters to dictionary. We do this so that at the end, 
      #we wont return coins with a value of 0.
      change['quarters'] = 0
      #if the value of leftover money is divisble by the coin, add one to the coin
      #in the dictionary and subtract the coin from money.
      while round(money/25,2)>=1:
        money = round(money-25)
        change['quarters']+=1
        
    elif money >= 10:
      change['dimes'] = 0 
      while round(money/10,2)>=1:
        money = round(money-10)
        change['dimes']+=1

    elif money >= 5:
      change['nickels'] = 0
      while round(money/5,2)>=1:
        money= round(money-5)
        change['nickels']+=1

    elif money >= 1:
      change['pennies'] = 0
      while round(money/1,2) >=1:
        money = round(money-1)
        change['pennies']+=1

  return(change)

print(makeChange(30))

assert makeChange(30) == {'quarters': 1, 'nickels': 1}

assert makeChange(10) == {'dimes': 1}

assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}

assert makeChange(100) == {'quarters': 4}

assert makeChange(125) == {'quarters': 5}

'''
#book answer
def makeChange(amount):

    # Create a dictionary to keep track of how many of each coin:

    change = ____

 

    # If the amount is enough to add quarters, add them:

    if amount >= ____:

        change['quarters'] = amount // ____

        # Reduce the amount by the value of the quarters added:

        amount = amount % ____

    # If the amount is enough to add dimes, add them:

    if amount >= ____:

        change['dimes'] = ____ // ____

        # Reduce the amount by the value of the dimes added:

        amount = ____ % ____

    # If the amount is enough to add nickels, add them:

    if amount >= ____:

        change['nickels'] = ____ // ____

        # Reduce the amount by the value of the nickels added:

        amount = ____ % ____

    # If the amount is enough to add pennies, add them:

    if amount >= 1:

        change[____] = amount

 

    return change
    '''
