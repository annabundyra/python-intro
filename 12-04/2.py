
numbers = [0, 5, 10, 15, 30]
def greater_than_five(number):
    if number > 5:
        return True
    else:
        return False

new_number_B = (list(filter(lambda number: number > 5, numbers)))