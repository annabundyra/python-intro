"""
Ways to Change a Banknote -- SOLUTION
"""



# NOTE = 10
# DENOM = [1, 5, 10, 25]
# WAYS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# D1 =    1  1  1  1  1  1  1  1  1  1  1
# D2 =    1
#
"""
Ways to Change a Banknote -- SOLUTION

"""

def num_ways(note, denoms):
    ways = [0 for amount in range(note + 1)]
    ways[0] = 1
    for num in denoms:
        for amount in range(1, note + 1):
            if num <= amount:
                ways[amount] += ways[amount - num]
    return ways[note]

print(num_ways(6, [1, 5]))