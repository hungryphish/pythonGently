#ord() converts a character string to unicode integer
#chr() convers a unicode int to a character string

'''
This function encrypts words by moving them over 13 spots in the alphabet
'''
def rot13(words):
  result=[]
  words=list(words)
  for c in range(len(words)):
    #If the character is not in the alphabet, return it.
    if words[c].isalpha()==False:
      result.append(words[c])
    else:
      #we seperate the upper and lower case letters because their
      #unicode numbers are different.
      if words[c].isupper() == True:
        if ord(words[c])+13 > 90:
          #the subtraction is that the letters loop back around. 
          result.append((chr(ord(words[c])+13-26)))
        else:
          result.append((chr(ord(words[c])+13)))
      else:
        if ord(words[c])+13 > 122:
          result.append((chr(ord(words[c])+13-26)))
        else:
          result.append((chr(ord(words[c])+13)))
        
  return(''.join(result))
print(rot13('Hello, world!'))

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'

assert rot13('Uryyb, jbeyq!') == 'Hello, world!'

assert rot13(rot13('Hello, world!')) == 'Hello, world!'

assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'

assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'


'''
#book solution


def rot13(text):

    # Create an encryptedText variable to store the encrypted string:

    encryptedText = ____

    # Loop over each character in the text:

    for character in text:

        # If the character is not a letter, add it as-is to encryptedText:

        if not character.____():

            encryptedText += ____

        # Otherwise calculate the letter's "rotated 13" letter:

        else:

            rotatedLetterOrdinal = ____(character) + 13

            # If adding 13 pushes the letter past Z, subtract 26:

            if ____.islower() and rotatedLetterOrdinal > ____:

                rotatedLetterOrdinal -= ____

            if ____.isupper() and rotatedLetterOrdinal > ____:

                rotatedLetterOrdinal -= ____

 

            # Add the encrypted letter to encryptedText:

            encryptedText += ____(rotatedLetterOrdinal)

 

    # Return the encrypted text:

    return encryptedText
    
'''
