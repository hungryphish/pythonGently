#returns a list of numbers between 1 and up to a user defined number, inclusive.
#if a number is divisible by 3, 5 or both, funciton will return Fizz, Buzz or fizzBuzz, in place of the number.
def fizzBuzz(upTo):
  l2=[] #empty list which is appended with fizz and buzz. Printed at end of function
  for i in list(range(1,upTo+1)): #creates the list which the if loop iterates through
    if i%3 == 0 and i%5==0:
      l2.append('fizzBuzz')
    elif i %3==0:
      l2.append('Fizz')
    elif(i %5==0):
      l2.append('Buzz')
    else:
      l2.append(i)
  print(l2)
  
fizzBuzz(5)
