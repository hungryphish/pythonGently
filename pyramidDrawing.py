'''
function that draws a pyramid with hastags. Height of pyramid is determined by user.
'''
def drawPyramid(height):
 for row in range(0,height): #number of rows to iterate through.
 #number of spaces is height - row + 1 because row starts at 0.
 #number of hashtags is just math. row 1 has 1, row 2 has 3, row 3 has 5
    print(' '*(height-(row+1))+'#'*(row*2+1)) 
drawPyramid(5)

'''book SOLUTION

def drawPyramid(height):

    # Loop over each row from 0 up to height:

    for rowNumber in range(____):

        # Create a string of spaces for the left side of the pyramid:

        leftSideSpaces = ' ' * (____ - (rowNumber + ____))

        # Create the string of hashtags for this row of the pyramid:

        pyramidRow = '#' * (____ * 2 + ____)

        # Print the left side spaces and the row of the pyramid:

        ____(leftSideSpaces + pyramidRow)
        '''
