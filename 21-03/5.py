

number = int(input('Enter a number in the range 5-10: '))

try:
    if number < 5 or number > 10:
        print("Exception will be raised")
        raise Exception

    division_result = 100 / number
    print(division_result)
    print("Well done")

except:
    print("Your number is not in the requested range")