def getSmallest(numbers):
  if len(numbers)<1:
    return(None)
  else:
    small = numbers[0]
    comp = small
    while len(numbers)>0:
      comp = numbers.pop()
      if small > comp:
        small=comp
      else:
        small=small
    return(small)
print(getSmallest([3, 2, 1]))
  
  
  
  
  





assert getSmallest([1, 2, 3]) == 1

assert getSmallest([3, 2, 1]) == 1

assert getSmallest([28, 25, 42, 2, 28]) == 2

assert getSmallest([1]) == 1

assert getSmallest([]) == None
