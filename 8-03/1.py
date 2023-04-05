#  Functions
# print("Hello World!")
# print("I hope the snow stops soon")

#  STRINGS
# 'Our example string object'.upper()
# 'Our example string object'.lower()
# 'Our example string object'.title()
# 'Our example string object'.count('o')
# 'our example string object'.capitalize()
# 'Our example string object'.endswith('ject')
# 'Our example string object'.endswith('mock')
# 'To make a nice cuppa you need: tea, milk, sugar and a cookie '.split(',')
# 'Our example string object'.replace('p', '#')
#  TASK TO COMPLETE TOGETHER: check built in methods available to use for strings
#
# 'string object' + . + click TAB

# oranges = 20
# cost_per_orange = 0.5
#
# total_cost = oranges * cost_per_orange
#
# print(str(oranges) + " oranges")
# print("costs £" + str(total_cost))

"""
In a new Python file called cat_food.py, create a program that calculates
how many cans of cat food you need to feed 10 cats.

Your will need:

A variable for the number of cats
A variable for the number of cans each cat eats in a day
A print() function to output the result
Extension: change the calculation to work out the amount needed for 7 days
"""
# cats = 10
# cans = 2
#
# total_cans = cats * cans
# total_cans_for_seven_days = total_cans * 7
#
# # output = str(cats) + " cats eat " + str(total_cans) + " cans."
# # output = "{} cats eat {} cans.".format(cats, total_cans)
# output = f"{cats} cats eat {total_cans} cans per day, and {total_cans_for_seven_days} for seven days!"
# print(output)

# STRING FORMATING - JOIN
# Show few examples on how to join strings together:
# my_words = ['Apple', 'Mango', 'Kiwi', 'Kiwi']
# '-'.join(my_words)
# ' '.join(my_words)
# ''.join(my_words)
#
# guests = ["Peter", "Mary", "Dave"]
# # message = f"We are going to the cinema with my classmates: {', '.join(guests)} and me"
# message = 'We\'re going to the cinema with my classmates: {} and me'.format(', '.join(guests))
# print(message)

# STRING SLICING

# s = 'a-b-c-d-e-f-g-h-i'
# s = s.split('-')
# print(s)
#
# sliced = s[-6:-2]
# print(sliced)

# print(s[-5:-2])

# s = "ABCDEFGHI"
# print(s[:3])
# s = "ABCDEFGHI"
# print(s[-3:])

s = "ABCDEFGHI"
print(s[-1])

#  IN BUILT functions
# print('Code')
# type('Code')
# len('Code')
# ord('C')
# chr(ord('C'))
# help('Code')
# help(type('Code'))