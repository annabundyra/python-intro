"""
All Possible Permutations -- SOLUTION

Please watch the demo video, which explains how to approach and solve
this challenge.

This is one of the multiple possible solutions (there might be many others)
This solution uses recursive approach.

This one is (roughly):
O(n*n!) time | O(n*n!) space
"""


def build_permutations(array, current, all_permutations):
    if not len(array) and len(current):
        all_permutations.append(current)
    else:
        for num in range(len(array)):
            new_array = array[:num] + array[num + 1:]
            new_perm = current + [array[num]]
            build_permutations(new_array, new_perm, all_permutations)


def get_permutations(array):
    all_permutations = []
    # build recursively
    build_permutations(array, current=[], all_permutations=all_permutations)
    return all_permutations

print(get_permutations([1, 2, 3]))