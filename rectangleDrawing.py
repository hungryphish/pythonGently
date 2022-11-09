'''a function to create a matrix of hashtags'''
def drawRectangle(width, height):
  #dont return anything if inputs are invalid
  if width < 1 or height <1:
    return()
  else:
    #print the number of # specified in width for each row specified in height.
    for h in range(0,height):
      print('#'*width)
drawRectangle(16, 4)

'''
#book solution.
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
