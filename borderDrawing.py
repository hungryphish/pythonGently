'''a function to create a matrix of hashtags'''
def drawBorder(width, height):
  #dont return anything if inputs are invalid
  if width < 2 or height <2:
    return()
  else:
    #Use the height variable to create rows.
    for row in range(0,height):
      #creating the top and bottom row. height-1 because we start at 0
        if row == 0 or row == height-1:
          print('+'+('-'*(width-2))+'+')
        #creating fill
        else:
          print('|'+(' '*(width-2))+'|')
        

drawBorder(2, 2)

'''
#Book solution
def drawBorder(width, height):

    # Special case: If the width or height is less than two, draw nothing:

    if width < ____ or height < ____:

        return

 

    # Print the top row:

    print('+' + ('-' * (width - ____)) + ____)

 

    # Loop for each row (except the top and bottom):

    for i in range(height - 2):

        # Print the sides:

        print(____ + (____ * (width - 2)) + ____)

 

    # Print the bottom row:

    print(___________________________________)
'''
