"""
TASK 1 (copy-paste this task in the dialog window to share with the student)

Given two lists a, b as follows: a =[4,5,7,3,5,6,3] and b = [3,7,0,56,4],
combine these two into one master list and then get rid of all duplicates
within the master list

NB: it is entirely up to you whether to write function or just write script
in the console.
"""

# EXAMPLE SOLUTION

a = [4, 5, 7, 3, 5, 6, 3]
b = [3, 7, 0, 56, 4]
a.extend(b)
result = set(a)
print(result)
# optionally you can covert your set back into a list
print(list(result))

###################################################


"""
TASK 2 (copy-paste this task in the dialog window to share with the student)

Take a string "Code" and print out all possible sub-strings of this word.
NB it is a tricky task, but we did something similar in a previous lesson.

NB: it is entirely up to you whether to write function or just write script
in the console.
"""

# You may need to help and navigate a student through the solution.

s = "Code"

for i in range(len(s)):  # it might be a little easier if you print i to understand what range(len(s)) produces
    for j in range(i, len(s)):  # it might be a little easier if you print j to understand what range(i, len(s)) produces
        substring = s[i: j + 1]  # effectively, this is slicing
        print(substring)
