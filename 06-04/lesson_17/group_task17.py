"""
Ways to Change a Banknote -- SOLUTION
"""



# NOTE = 10
# DENOM = [1, 5, 10, 25]
# WAYS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# D1 =    1  1  1  1  1  1  1  1  1  1  1
# D2 =    1
#
def num_ways(note, denom):
   ways = [0 for amount in range(note + 1)]
   ways[0] = 1

   for number in denom:
      for amount in range(1, note + 1):
         if number <= amount:
            ways[amount] = ways[amount] + ways[amount-denom]
      return ways[note]

print(num_ways(6, [1,5]))
