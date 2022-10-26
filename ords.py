#making a function to add ordinals to the end of numbers. e.g. turn 1 into 1st.
def ordinalSuffix(number):
  number = str(number) #converts the number to a string so it can be sliced.
  if float((number)[-2:]) > 9 and float((number)[-2:]) < 20 or float((number)[-1:]) == 0 or float((number)[-1:]) > 3: #slices number and converts the sliced number to a float in order to make a comparison.
    return (number+'th')  #returns the original number and the suffix e.g. 1st
  elif float((number)[-1:]) == 1:
    return (number+'st')
  elif float((number)[-1:]) == 2:
    return (number+'nd')
  elif float((number)[-1:]) == 3:
    return (number+'rd')
print(ordinalSuffix(133))
