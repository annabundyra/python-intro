from functools import reduce

numbers = [0, 5, 10, 20, 30, 40]
print(numbers)

def sum_up(a, b):
    return  a + b

result_A = reduce(sum_up, numbers)
print(result_A)

result_B = reduce(lambda a, b: a + b, numbers)
print(result_B)