
################################################
###           PALINDROME EXERCISE            ###
################################################

"""
Palindrome Check

Write a function that takes a non-empty string
and that returns a boolean representing whether the string is a palindrome.

Think and plan your solution first.
If helps, write a pseudo-code.
"""

# def isPalindrome(string):
#
#     # your solution here
#
#
# print(isPalindrome('hannah'))  # should return True
#
# print(isPalindrome('mummy'))  # should return False
#
# print(isPalindrome('I'))  # should return True


'''
Solution 1 --> this solution is OK, it is correct and works
'''
#
# def isPalindrome(string):
#     l = len(string)
#     if l == 1:
#         return True
#     return string == string[::-1]
#
#
#
# print(isPalindrome('hannah')) # should return True
#
# print(isPalindrome('mummy')) # should return False
#
# print(isPalindrome('I')) # should return True


'''
Solution 1 -- even shorter
'''
#
# def isPalindrome(string):
#     return string == string[::-1]
#
#
#
# print(isPalindrome('hannah')) # should return True
#
# print(isPalindrome('mummy')) # should return False
#
# print(isPalindrome('I')) # should return True

"""
Solution 2 --> this solution is excellent and very efficient!
"""

# def isPalindrome(string):
#     leftIdx = 0
#     rightIdx = len(string) - 1
#     while leftIdx < rightIdx:
#         if string[leftIdx] != string[rightIdx]:
#             return False
#         leftIdx += 1
#         rightIdx -= 1
#     return True
#
# print(isPalindrome('hannah')) # should return True
#
# print(isPalindrome('mummy')) # should return False
#
# print(isPalindrome('I')) # should return True