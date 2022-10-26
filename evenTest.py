#test if a number is even or odd
def isOdd(n):
  return((n%2) == 1)
def isEven(n):
  return((n%2) == 0)

assert isOdd(42) == False

assert isOdd(9999) == True

assert isOdd(-10) == False

assert isOdd(-11) == True

assert isOdd(3.1415) == False

assert isEven(42) == True

assert isEven(9999) == False

assert isEven(-10) == True

assert isEven(-11) == False

assert isEven(3.1415) == False
x=3.1415
print(isEven(x))
print(x%2)
