'''function converts a lower case string to an upeer case string'''

def getUppercase(word):
  #create a dictionary to reference
  letters={'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}
  #create empty string which will be answer.
  newWord=''
  #iterate through each character in the word.
  for c in range(0,len(word)):
    #test if character is a lower case letter. No need to convert if it isnt.
    if word[c] in letters.keys():
      #Using the character as a key, store the resulting upper case leter in a variable.
      charc=letters[word[c]]
    else:
      #since there is no need to convert, store character in a variable.
      charc=word[c]
    #Concatenate variable onto the new word
    newWord=newWord+charc
  return(newWord)

    
print(getUppercase('fart32'))


assert getUppercase('Hello') == 'HELLO'

assert getUppercase('hello') == 'HELLO'

assert getUppercase('HELLO') == 'HELLO'

assert getUppercase('Hello, world!') == 'HELLO, WORLD!'

assert getUppercase('goodbye 123!') == 'GOODBYE 123!'

assert getUppercase('12345') == '12345'

assert getUppercase('') == ''

'''
#book answer
# Map the lowercase letters to uppercase letters.

LOWER_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

 

def getUppercase(text):

    # Create a new variable that starts as a blank string and will

    # hold the uppercase form of text:

    uppercaseText = ''

    # Loop over all the characters in text, adding non-lowercase

    # characters to our new string:

    for character in ____:

        if character in ____:

            # Append the uppercase form to the new string:

            uppercaseText += ____[____]

        else:

            uppercaseText += ____

 

    # Return the uppercase string:

    return ____
  '''
