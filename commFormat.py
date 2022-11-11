'''this function turns a float or integer into a string with comma seperated thousands.'''
def commaFormat(number):
  #tests is number is less than a thousand.If so, just return number as string.
  if abs(number) < 999:
    return(str(number))
  else:
    #convert number to a string.
    number=str(number)
    #test if there are decimals. If so, we split them off the rest of the string so that no commas are included past the decimal.
    if number.find('.')> -1:
      dec = number[number.find('.'):]
      number = number[:number.find('.')]
    else:
      dec=''
    #find out how many commas will be placed.
    coms =len(number)//3
    #loop to add commas.
    for i in range(coms):
      #Math is there to add a comma for every thousands place. -1 i is included so that each loop accounts for the previous comma.
      number=number[:((i+1)*-3)-i]+','+number[((i+1)*-3)-i:]
    #tests if the first character in the string is a comma. This is possible because of the previous math.
    #Overwrites string to include all characters after comma.
    if number[0]==',':
      number=number[1:]
    return(number+dec)
    
print(commaFormat(100000000))



assert commaFormat(1) == '1'

assert commaFormat(10) == '10'

assert commaFormat(100) == '100'

assert commaFormat(1000) == '1,000'

assert commaFormat(10000) == '10,000'

assert commaFormat(100000) == '100,000'

assert commaFormat(1000000) == '1,000,000'

assert commaFormat(1234567890) == '1,234,567,890'

assert commaFormat(1000.123456) == '1,000.123456'


'''
#book answer
    # Convert the number to a string:

    number = str(____)

 

    # Remember the fractional part and remove it from the number, if any:

    if '.' in ____:

        fractionalPart = number[number.index(____):]

        number = number[:number.index('.')]

    else:

        fractionalPart = ''

 

    # Create a variable to hold triplets of digits and the

    # comma-formatted string as it is built:

    triplet = ____

    commaNumber = ____

 

    # Loop over the digits starting on the right side and going left:

    for i in range(len(number) - 1, ____, ____):

        # Add the digits to the triplet variable:

        triplet = ____[i] + ____

        # When the triplet variable has three digits, add it with a

        # comma to the comma-formatted string:

        if ____(triplet) == ____:

            commaNumber = triplet + ',' + ____

            # Reset the triplet variable back to a blank string:

            triplet = ____

 

    # If the triplet has any digits left over, add it with a comma

    # to the comma-formatted string:

    if triplet != '':

        commaNumber = ____ + ',' + ____

 

    # Return the comma-formatted string:

    return ____[:____] + fractionalPart
    '''
