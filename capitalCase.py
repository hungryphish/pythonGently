'''function converts a string into capital case.'''

def getTitleCase(words):
  #blank string to append.
  newWords=''
  #loop through index of all characters in string
  for c in range(0,len(words)):
    #Test if char before is a letter or if it is the beginning of the string. Both should be capitals
    if words[c-1].isalpha() == False or c < 1:
      character=words[c].upper()
    #test if char before is a letterm if so, it should not be capitalized.
    elif words[c-1].isalpha()==True:
      character = words[c].lower()
    #Should just return non-letters
    else:
      character=words[c]
    #characters to string.
    newWords=newWords+character
  return(newWords)

print(getTitleCase('HELLO'))




assert getTitleCase('Hello, world!') == 'Hello, World!'

assert getTitleCase('HELLO') == 'Hello'

assert getTitleCase('hello') == 'Hello'

assert getTitleCase('hElLo') == 'Hello'

assert getTitleCase('') == ''

assert getTitleCase('abc123xyz') == 'Abc123Xyz'

assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'

assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'


'''
#book solution
def getTitleCase(text):

    # Create a titledText variable to store the titlecase text:

    titledText = ____

    # Loop over every index in text:

    for i in range(len(____)):

        # The character at the start of text should be uppercase:

        if i == ____:

            titledText += text[i].____()

        # If the character is a letter and the previous character is

        # not a letter, make it uppercase:

        elif text[____].isalpha() and not text[i - ____].isalpha():

            titledText += text[____].upper()

        # Otherwise, make it lowercase:

        else:

            titledText += text[i].____()

    # Return the titled cased string:

    return titledText
    '''
