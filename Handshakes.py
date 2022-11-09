def printHandshakes(people):
  x=" shakes hands with "
  i=0
  while len(people)>1:
    for p in people:
      name=people.pop(0)
      for p in range(0,len(people)):
        print(name+x+people[p])
        i+=1
  return(i)
printHandshakes(['Alice', 'Bob', 'Carol', 'David'])

assert printHandshakes(['Alice', 'Bob']) == 1

assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3

assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6

#Book answer

'''
def printHandshakes(people):

    # The total number of handshakes starts at 0:

    numberOfHandshakes = ____

    # Loop over every index in the people list except the last:

    for i in range(0, len(____) - 1):

        # Loop over every index in the people list after index i:

        for j in range(i + ____, len(____)):

            # Print a handshake between the people at index i and j:

            print(people[____], 'shakes hands with', people[____])

            # Increment the total number of handshakes:

            numberOfHandshakes += ____

    # Return the total number of handshakes:

    return numberOfHandshakes
    '''
