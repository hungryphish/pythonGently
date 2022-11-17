def mergeXLists(listOfLists):
  lst1=listOfLists[0]    #i
  lst2=listOfLists[1]  #j
  results=[]
  i=0
  j=0
  while i < len(lst1) and j < len(lst2):
    if lst1[i]<lst2[j]:
      results.append(lst1[i])
      i+=1
    else:
      results.append(lst2[j])
      j+=1
  while i < len(lst1):
    if j >= len(lst2):
      results.append(lst1[i])
      i+=1        
  while j < len(lst2):
    if i >= len(lst1):
      results.append(lst2[j])
      j+=1        
      
  return(results)
print(f'list is {mergeXLists([[15,24,56],[17,42,62,73,82]])}')

assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]

assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]

assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]

assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]

'''
#book answer

    # Create an empty list to hold the final sorted results:

    result = ____

 

    # Start i1 and i2 at index 0, the start of list1 and list2:

    i1 = ____

    i2 = ____

 

    # Keeping moving up i1 and i2 until one reaches the end of its list:

    while i1 < len(____) and ____ < len(list2):

        # Add the smaller of the two current items to the result:

        if list1[____] < list2[____]:

            # Add list1's current item to the result:

            result.append(____[i1])

            # Increment i1:

            i1 += ____

        else:

            # Add list2's current item to the result:

            result.append(____[i2])

            # Increment i2:

            i2 += ____

 

    # If i1 is not at the end of list1, add the remaining items from list1:

    if i1 < len(____):

        for j in range(i1, len(list1)):

            result.append(____[j])

    # If i2 is not at the end of list2, add the remaining items from list2:

    if i2 < len(____):

        for j in range(i2, len(list2)):

            result.append(____[j])

 

    # Return the merged, sorted list:

    return result
'''
