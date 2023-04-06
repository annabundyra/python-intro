"""
TASK 1 (copy-paste this task in the dialog window to share with the student)

Write a function that accepts a number as an input and returns
a list of integers that stretch from 0 up to the given number
(including the number!) in the increments of 5. But your list must EXCLUDE
any numbers that can be divided by 7 without a remainder.

1. We only pass one integer to the function that is int > 0

"""

# EXAMPLE SOLUTION
def func(num):
    i = 0
    divided_list = []
    for i in range(0, num + 1, 5):
        if i % 7 != 0:
            divided_list.append(i)
        i += 1
    return divided_list
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



# EXAMPLE SOLUTION
def mult_func(x, y):
    result = 0
    for i in range(x):
        result += y
    return result


print(mult_func(5, 4))
print(mult_func(7, 6))
print(mult_func(8, 3))
