#chessboard is 8x8,0-7, top left is white

#create a function which identifies the color of a square on a chessboard, given column and row.
def getChessSquareColor(column,row):
  if column > 8 or row > 8 or column <1 or row <1: #creates boundaries. of board
    return('')
  elif (column+row)%2 > 0: #if the sum of column and row is even, return black, odd, white.
    return('black')
  else:
    return('white')

print(getChessSquareColor(4,5))

  
assert getChessSquareColor(1, 1) == 'white'

assert getChessSquareColor(2, 1) == 'black'

assert getChessSquareColor(1, 2) == 'black'

assert getChessSquareColor(8, 8) == 'white'

assert getChessSquareColor(0, 8) == ''

assert getChessSquareColor(2, 9) == ''
