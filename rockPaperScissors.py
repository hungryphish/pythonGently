''' 
Function that simulatees rock paper scissors.
If both entries are valid, will return either who won, or that it is a tie.
'''

def rpsWinner(player1, player2):
  #put answers into a list to make it easy to search
  round=[player1,player2]
  #put valid moves into a list to make it easy to search
  moves=['rock', 'paper', 'scissors']
  
  #check to ensure both player moves are valid
  if player1 and player2 in moves:
    #checks to see if there are win conditions.
    if 'rock' in round and 'scissors' in round:
      winner=round.index('rock')
    elif 'scissors' in round and 'paper' in round:
      winner=round.index('scissors')
    elif 'paper' in round and 'rock' in round:
      winner=round.index('paper')
    #no win conditions. Return tie.
    else:
      return('tie')
    #takes index returned from win condition and determines who won.
    if winner == 0:
      return('player one')
    elif winner == 1:
      return('player two')
  else:
    return('Invalid')
  
print(rpsWinner('rock','paper'))

assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'

'''
book solution

def rpsWinner(move1, move2):

    # Check all six possible combinations with a winner and return it:

    if move1 == 'rock' and move2 == 'paper':

        return 'player two'

    elif ____ == 'rock' and move2 == 'scissors':

        return ____

    ____ move1 == 'paper' and ____ == 'scissors':

        return ____

    ____ ____ == 'paper' and move2 == 'rock':

        return ____

    ____ move1 == 'scissors' and ____ == 'rock':

        return ____

    ____ ____ == 'scissors' and  ____ == 'paper':

        return 'player one'

    # For all other combinations, it is a tie:

    ____:

        return ____
    '''
