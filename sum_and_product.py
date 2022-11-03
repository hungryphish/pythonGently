'''
function returns the sum of all numbers in a list. If an empty list is provided, returns 0.
'''

def calculateSum(nums):
  result=()
  if len(nums)==0:
    result=0
  else:
    count = 0
    result= 0
    while count < len(nums):
      result=result+nums[count]
      count = count + 1
  return(result)

print(calculateSum([1,2,3,4,5,6,7,8,9,10]))

assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30

'''
function returns the product of all numbers in a list. If an empty list is provided, returns 1.
'''
# def calculateProduct(nums):
#   #reurning 1 if empty.
#   if len(nums)==0:
#     result=1
#   #multiplication
#   else:
#     #set count to 1. It will be the index of the number used to multipy.
#     count = 1
#     #result is 0. index of first number in list. Adds to move through list.
#     result = nums[0]
#     #iterate through list as long as there are more numbers.
#     while count < len(nums):
#       #multiply the first number by the second.
#       result= result*nums[count]
#       #advance in list
#       count = count + 1
# #   return(result)

'''
correct function accrding to book
'''
def calculateProduct(numbers):
    # Start the product result at 1:
    result = 1
    # Loop over all the numbers in the numbers parameter, and multiply
    # them by the running product result:
    for number in numbers:
        result = number * result
    # Return the final product result:
    return(result)
print(calculateProduct([1,2,3,4,5,6,7,8,9,10]))

assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840
