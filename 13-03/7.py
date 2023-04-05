import random

def flip_coin():
    random_number = random.randint(1,2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
        return side

choice = input('heads or tails: ')
result = flip_coin()

if(choice == result):
    print("Win")
else:
    print("Not win!")