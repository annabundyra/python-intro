import random

sides = int(input("How many slides does the die have?"))
random_int = random.randint(1, sides)

print(f"You rolled a {random_int}")