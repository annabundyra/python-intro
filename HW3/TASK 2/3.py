

import random
import numpy as np

number = input("What number are you trying to get? ")

throws_number = 100
dice_number = 2
throws = np.random.randint(1,7, size=(throws_number, dice_number))

sum_throws = np.sum(throws,axis=1)

probability = (np.count_nonzero(sum_throws == int(number)))

print(f"The chance of you getting {number} is {probability/100}%")