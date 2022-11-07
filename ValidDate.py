'''
User provides a year month and date. Function determines supplied date is valid.
First checks if the month is February and if it is a leap year to see if day is valid.
'''

#function to determine if it is a leap year.
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

#list of months that have 31 days and months that have 30 days.
months31=[1,3,5,7,8,9,12]
months30=[4,6,10,11]

    
def isValidDate(year,month,day):
  #If user is looking at February, then we will see if it is a leap year.
  if month == 2:
    febDays = isLeapYear(year)
    if febDays == True:
      if day > 29 or day < 1:
        return(False)
      else:
        return(True)
    else:
      if day > 28  or day < 1:
        return(False)
      else:
        return(True)
  #If a month is in the 31 list, check if day variable exceeds 31
  elif month in months31:
    if day > 31 or day < 1:
      return(False)
    else:
      return(True)
  #If a month is in the 30 list, check if day variable exceeds 30
  elif month in months30:
    if day > 30 or day < 1:
      return(False)
    else:
      return(True)
  else:
    return(False)
    
print(isValidDate(1666, 4, 0))

assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False

# Import the leapyear module for its isLeapYear() function:

____ leapyear

 
'''Book Solution
def isValidDate(year, month, day):

    # If month is outside the bounds of 1 to 12, return False:

    if not (1 ____ month ____ 12):

        return ____

    # After this point, you can assume the month is valid.

 

    # If the year is a leap year and the date is Feb 29th, it is valid:

    if leapyear.isLeapYear(____) and ____ == 2 and ____ == 29:

        return ____

    # After this point, you can assume the year is not a leap year.

 

    # Check for invalid dates in 31-day months:

    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= ____ <= 31):

        return ____

    # Check for invalid dates in 30-day months:

    elif ____ in (4, 6, 9, 11) and not (1 <= day <= 30):

        return ____

    # Check for invalid dates in February:

    elif month == ____ and not (1 <= ____ <= 28):

        return ____

 

    # Date passes all checks and is valid, so return True:

    return ____'''
