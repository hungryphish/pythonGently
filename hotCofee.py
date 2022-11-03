'''
determines total cost of coffe bill, when every 8th purchased cup is free.
'''

def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
  #divide by 9 because the ninth purchased cup is free.
  free=(numberOfCoffees//9) * pricePerCoffee
  result=numberOfCoffees*pricePerCoffee-free
  return(result)
  


print(getCostOfCoffee(9,2.50))

assert getCostOfCoffee(7, 2.50) == 17.50

assert getCostOfCoffee(8, 2.50) == 20

assert getCostOfCoffee(9, 2.50) == 20

assert getCostOfCoffee(10, 2.50) == 22.50

 

for i in range(1, 4):

    assert getCostOfCoffee(0, i) == 0

    assert getCostOfCoffee(8, i) == 8 * i

    assert getCostOfCoffee(9, i) == 8 * i

    assert getCostOfCoffee(18, i) == 16 * i

    assert getCostOfCoffee(19, i) == 17 * i

    assert getCostOfCoffee(30, i) == 27 * i
    

#book solution
'''    
Solution Template

Try to first write a solution from scratch. But if you have difficulty, you can use the following partial program as a starting place. Copy the following code from https://invpy.com/buy8get1free-template.py and paste it into your code editor. Replace the underscores with code to make a working program:

def getCostOfCoffee(numberOfCoffees, pricePerCoffee):

    # Track the total price:

    totalPrice = ____

    # Track how many coffees we have until we get a free one:

    cupsUntilFreeCoffee = 8

 

    # Loop until the number of coffees to buy reaches 0:

    while numberOfCoffees ____ 0:

        # Decrement the number of coffees left to buy:

        ____ -= 1

 

        # If this cup of coffee is free, reset the number to buy until

        # a free cup back to 8:

        if cupsUntilFreeCoffee == ____:

            ____ = 8

        # Otherwise, pay for a cup of coffee:

        else:

            # Increase the total price:

            totalPrice += ____

            # Decrement the coffees left until we get a free coffee:

            cupsUntilFreeCoffee -= ____

 

    # Return the total price:

    return ____

The complete solution for this exercise is given in Appendix A and https://invpy.com/buy8get1free.py. You can view each step of this program as it runs under a debugger at https://invpy.com/buy8get1free-debug/.

Another Solution Design

The counting solution design, while simple, gets slower the larger the number of purchased coffees becomes. If you called getCostOfCoffee(1000000000, 2.50) it could take a couple of minutes before the function returns an answer. There’s a more direct way to calculate the total price for these large coffee orders.

First, you can calculate the number of free coffees by integer dividing numberOfCoffees by 9. For every nine coffees, one is a free coffee. Any remainder coffees don’t matter for counting the number of free coffees, which is why you use the // integer division operator instead of the / regular division operator. Store this division result in a variable named numberOfFreeCoffees.

To calculate the number of paid coffees, subtract numberOfFreeCoffees from numberOfCoffees and store this difference in a variable named numberOfPaidCoffees. (This makes sense; coffees are either paid for or free, so the number of paid and free coffees must add up to numberOfCoffees). The final value to return is the numberOfPaidCoffees times the pricePerCoffee.

The benefit of this solution design is that it does three calculations (a division, a subtraction, and a multiplication) no matter how big or small numberOfCoffees. Calling getCostOfCoffee(1000000000, 2.50) with this implementation finishes in milliseconds rather than minutes.

Another Solution Template

Try to first write a solution from scratch. But if you have difficulty, you can use the following partial program as a starting place. Copy the following code from https://invpy.com/buy8get1free2-template.py and paste it into your code editor. Replace the underscores with code to make a working program:

def getCostOfCoffee(numberOfCoffees, pricePerCoffee):

    # Calculate the number of free coffees we get in this order:

    numberOfFreeCoffees = ____ // 9

 

    # Calculate the number of coffees we will have to pay for in this order:

    numberOfPaidCoffees = numberOfCoffees - ____

 

    # Calculate and return the price:

    return ____ * ____
    '''
