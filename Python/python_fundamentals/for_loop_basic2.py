# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
# def Biggie(arr):
#   for i in range(len(arr)):
#     if arr[i] > 0:
#       arr[i] = "big"
#   return arr
# print(Biggie([-1, 3, 5, -5]))

# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to b a positive number).
# def CountPositives(arr):
#   count = 0
#   for i in range(len(arr)):
#     if i > 0:
#       count += 1
#   arr[len(arr) - 1] = count
#   return arr
# print(CountPositives([-1,1,1,1]))  

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
# def SumTotal(arr):
#   sum = 0
#   for i in arr:
#     sum += i
#   return sum
# print(SumTotal([1,2,3,4]))

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
# def Average(arr):
#   sum = 0
#   for i in arr:
#     sum += i
#   avg = sum/len(arr)
#   return avg
# print(Average([1,2,3,4]))

# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4
# def Length(arr):
#   return len(arr)
# print(Length([1,2,3,4]))

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
# def Minimum(arr):
#   min = arr[0]
#   if len(arr) == 0:
#     return 'false'
#   else: 
#     for i in arr:
#       if i < min:
#         min = i
#   return min
# print(Minimum([2,1,4,5]))

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -3.
# def Maximum(arr):
#   max = arr[0]
#   if len(arr) == 0:
#     return 'false'
#   else: 
#     for i in arr:
#       if i > max:
#         max = i
#   return max
# print(Maximum([2,1,4,5]))

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
# def Ultimate(arr):
#   Dict = {}
#   sumTotal = 0
#   minimum = arr[0]
#   maximum = arr[0]

#   for i in arr:
#     if i < minimum:
#       minimum = i
#     if i > maximum:
#       maximum = i
#     sumTotal += i
#   Dict["sum"] = sumTotal
#   Dict["average"] = sumTotal/len(arr)
#   Dict["minimum"] = minimum
#   Dict["maximum"] = maximum
#   Dict["length of array"] = len(arr)
#   return Dict 
# print(Ultimate([1,2,3,4,5,6,7,8,9]))

# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
# def ReverseList(arr):
#   temp = 0
#   for i in range(int(len(arr)/2)):
#     temp = arr[i]
#     arr[i] = arr[len(arr) - (i+1)]
#     arr[len(arr) - (i+1)] = temp
#   return arr
# print(ReverseList([1,2,3,4]))


