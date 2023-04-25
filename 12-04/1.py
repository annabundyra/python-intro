
my_list = [2, 4, 6, 8]
print(my_list)

def add_five(number):
    return number + 5

new_list_A = list(map(add_five, my_list))
print(new_list_A)

new_list_B = list(map(lambda x: x + 5, my_list))
print(new_list_B)