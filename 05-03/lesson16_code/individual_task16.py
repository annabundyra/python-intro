"""
Move Target Number -- SOLUTION

Please watch the demo video, which explains how to approach and solve
this challenge.

This is one of the multiple possible solutions (there might be many others)

This one is:
O(n) time | O(1) space - where n is the length of the array
"""


def move_num_to_end(array, target):
    x = 0
    y = len(array) - 1
    while x < y:
        while x < y and array[y] == target:
            y -= 1
        if array[x] == target:
            array[x], array[y] = array[y], array[x]
        x += 1
    return array

number = 2 

my_list = [2,1,2,2,2,3,4,2] 

print(move_num_to_end(array=my_list, target=number))
