import unittest

# def reverseList(list):
#     for i in range(int(len(list)/2)):
#         list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
#     return list

# def isPalindrome(str):
#     for i in range(int(len(str)/2)):
#         if str[i] == str[len(str)-i-1]:
#             continue
#         else:
#             return False
#     return True

# def coins(change):
#     # pass
#     coin = [0, 0, 0, 0]
#     if change >= 25:
#         coin[0] = int(change/25)
#         change -= coin[0] * 25
#     if change >= 10:
#         coin[1] = int(change/10)
#         change -= coin[1] * 10
#     if change >= 5:
#         coin[2] = int(change/5)
#         change -= coin[2] * 5
#     coin[3] = change
#     return coin

# def Factorial(num):
#     sum = 1
#     for i in range(1, num+1):
#         if num > 0:
#             sum *= i
#     return sum

def Fib(n):
  if n <= 1:
    return [0, 1]
  else:
    x = Fib(n - 1)
    print(x)
    x.append(x[len(x) - 1] + x[len(x) - 2])
    return x

# class reverseListTests(unittest.TestCase):
#     def testOne(self):
#         return self.assertEqual(reverseList([1,3,5]), [5,3,1])
#     def testTwo(self):
#         return self.assertEqual(reverseList([7,9,11,13]), [13,11,9,7])
#     def testThree(self):
#         return self.assertEqual(reverseList([4,0,0,0,0,0,0]), [0,0,0,0,0,0,4])
# if __name__ == "__main__":
#     unittest.main()

# class isPalindromeTests(unittest.TestCase):
#     def testOne(self):
#         return self.assertEqual(isPalindrome("racecar"), True)
#     def testTwo(self):
#         return self.assertEqual(isPalindrome("rabcr"), False)
#     def testThree(self):
#         return self.assertEqual(isPalindrome("lolol"), True)
# if __name__ == "__main__":
#     unittest.main()

# class coinsTest(unittest.TestCase):
#     def testOne(self):
#         return self.assertEqual(coins(87), [3, 1, 0, 2])
#     def testTwo(self):
#         return self.assertEqual(coins(99), [3, 2, 0, 4])
#     def testThree(self):
#         return self.assertEqual(coins(56), [2, 0, 1, 1])
# if __name__ == "__main__":
#     unittest.main()

# class FactorialTest(unittest.TestCase):
#     def testOne(self):
#         return self.assertEqual(Factorial(5), 120)
#     def testTwo(self):
#         return self.assertEqual(Factorial(6), 720)
#     def testThree(self):
#         return self.assertEqual(Factorial(7), 5040)
# if __name__ == "__main__":
#     unittest.main()

class FibTest(unittest.TestCase):
    def testOne(self):
        return self.assertEqual(Fib(5), [0,1,1,2,3,5])
    def testTwo(self):
        return self.assertEqual(Fib(6), [0,1,1,2,3,5,8])
    def testThree(self):
        return self.assertEqual(Fib(7), [0,1,1,2,3,5,8,13])
if __name__ == "__main__":
    unittest.main()


# reverseList - Write a function that reverses the values in the list (without creating a temporary listay).  For example, reverseList([1,3,5]) should return [5,3,1].  In other words assertEqual( reverseList[1,3,5], [5,3,1] ).  Create at least 3 other test cases before you implement the functionality.

# isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).  For example, isPalindrome("racecar") should return true.  Another way to say this is assertEqual( isPalindrome("racecar"), True ) or assertTrue( isPalindrome("racecar")).  Similarly, assertFalse( isPalindrome("rabcr") ).  Add at least 5 other test cases before you implement the functionality.  Remember that you need to write the tests first, make sure the tests fail, and then write the functionality within the function, to now make all the tests pass.  (also remember that if a = "hello", a[0] returns 'h' and a[1] returns 'e').

# coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.  For example, if you need to give the customer 87 cents, you can give 3 quarters, 1 dime, 0 nickel and 2 pennies.  If you need to give the customer 92 cents, you can give 3 quarters, 1 dime, 1 nickel, and 2 pennies.  Write the function such that for example, coin(87) returns [3,1,0,2].  coin(92) should return [3,1,1,2].  Add at least 5 other test cases first, before you fill in the codes inside function coin().

# Factorial (hacker challenge).  Write a function factorial() that returns the factorial of the given number.  For example, factorial(5) should return 120.  Do this using recursion; remember that factorial(n) = n * factorial(n-1).

# Fib (hacker challenge). Write a function fib() in Python that returns the appropriate Fibonacci number.  Do this using recursion.  Let's say that the first two Fibonacci numbers are 0 and 1.  Remember that fib(n) = fib(n-2) + fib(n-1).