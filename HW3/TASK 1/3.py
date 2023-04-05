
number = input("Give a number: ")
number = list(number)

units = ['One', 'Two', 'Three', 'Four', 'Five',
         'Six', 'Seven', 'Eight', 'Nine', "Ten"]

ten = int(number[0])
one = int(number[1])

ten_str = units[ten - 1]
one_str = units[one - 1]

if(ten == 1):
    if (one == 1):
        print(f"{ten_str} Ten, {one_str} One")
    else:
        print(f"{ten_str} Ten, {one_str} Ones")
else:
    if(one == 1):
        print(f"{ten_str} Tens, {one_str} One")
    else:
        print(f"{ten_str} Tens, {one_str} Ones")