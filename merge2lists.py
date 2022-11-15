def mergeTwoLists(l1, l2):
  answer =[]
  l1num = 0
  l2num = 0
  #loop until the answer list is populated with both lists.
  while len(answer)<(len(l1)+len(l2)):
    #makes sure function wont try to add indices that dont exist.
    #don't need to do this for l2 on this line because we do it inside the loop.
    if l1num < len(l1):
      #makes sure dunction wont try to add indices that dont exist in list 2. 
      #checks for next lowest number in each list.
      # if number is from L1 it will append to the answer list
      if l2num >= len(l2) or l1[l1num] < l2[l2num]:
        answer.append(l1[l1num])
        l1num+=1
      #if number is from list 2 it ill append to answer list.
      else:
        answer.append(l2[l2num])
        l2num+=1
  return(answer)
print(mergeTwoLists([4, 5], [1, 2, 3]))


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
