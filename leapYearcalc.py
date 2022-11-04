'''
User provides a year. Function determines if it is a leap year.
Leap years occur on years divsible by 4 except for years divisible by 100 except for years divisible by 400.
'''

def isLeapYear(year):
  #is the year divisible by 4?
  if year%4==0:
    #is it also divisible by 100?
    if year%100==0:
      #is it also divisible by 400?
      if year%400==0:
        return(True)
      else:
        return(False)
    else:
      return(True)
  else:
    return(False)
  
print(isLeapYear(2004))

assert isLeapYear(1999) == False

assert isLeapYear(2000) == True

assert isLeapYear(2001) == False

assert isLeapYear(2004) == True

assert isLeapYear(2100) == False

assert isLeapYear(2400) == True
