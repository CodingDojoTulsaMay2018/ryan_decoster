# Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].
# def Countdown(x):
#   newarr = []
#   for i in range(x,-1,-1):
#     newarr.append(i)
#   return newarr
# print(Countdown(5))

# Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.
# def PrintReturn(a,b):
#   print(a)
#   return b
# print(PrintReturn(1,2))

# First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.
# def FirstLength(arr):
#   return arr[0] + len(arr)
# print(FirstLength([1,2,3,4,5]))

# Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only element long, have the function return False
# def GreaterThanSec(arr):
#   if len(arr) <= 1:
#     return 'false'
#   x = arr[1]
#   newarr = []
#   count = 0
#   for i in arr:
#     if i > x:
#       newarr.append(i)
#       count += 1
#   print(count)
#   return newarr
# print(GreaterThanSec([1,2,3,4,5,6]))

# This Length, That Value - Given two numbers, return array of length num1 with each value num2.  Print "Jinx!" if they are same.
# def ThisLength(x,y):
#   if x == y:
#     print("Jinx!")
#   newarr = []
#   for i in range(x):
#     newarr.append(y)
#   return newarr
# print(ThisLength(5,6))