"""
TASK 1 (copy-paste this task in the dialog window to share with the student)

Write a function that accepts a number as an input and returns
a list of integers that stretch from 0 up to the given number
(including the number!) in the increments of 5. But your list must EXCLUDE
any numbers that can be divided by 7 without a remainder.

1. We only pass one integer to the function that is int > 0

"""

"""
THINGS TO PAY ATTENTION TO:

1. See if a student asks for an example input and output OR even better, if 
a student suggests / comes up with their own input-output. 

Here is an example: 
--------------------
Input: 50
Output: [5, 10, 15, 20, 25, 30, 40, 45, 50]

NB: the result list excludes 0 and 35, because:

 0 divide by 7 is 0 (no remainder)
 35 divide by 7 is 5 (no remainder)

"""


# EXAMPLE SOLUTION
def func(num):
    result = [i for i in range(0, num+1, 5) if i % 7 != 0]
    return result

"""
Student's solution can be written in ANY way, as long as it work correctly

range(0, num+1, 5) --> gives you a range of numbers from 0 to the given number
in increments of 5 (NB: num + 1, so that the actual number is also included)

if i % 7 != 0 --> the if condition allows to exclude numbers that 
are divisible by 7
"""

print(func(50))

############################################################################

"""
TASK 2 (copy-paste this task in the dialog window to share with the student)

Write a function that will take two whole numbers (integers) as 
input and output. The  function returns the result of multiplying these two 
numbers together. For example 5 * 4 = 20

However, to make this task more challenging, you have to assume the * key of 
your keyboard is broken or missing and hence you are not allowed to use the * 
operator in your code!!!

"""

"""
ONLY IF a student is struggling, give them a HINT:

5 * 4 = 5 + 5 + 5 + 5
7 * 6 = 7 + 7 + 7 + 7 + 7 +7
8 * 3 = 8 + 8 +8
"""


# EXAMPLE SOLUTION
def mult_func(x, y):
    result = 0
    for num in range(y):
        result += x
    return result


print(mult_func(5, 4))
print(mult_func(7, 6))
print(mult_func(8, 3))
