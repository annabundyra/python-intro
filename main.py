print("Hello world!")

cats = 10
cans = 2
weeks = 7

total_cans = weeks * cats * cans


output = str(cats) + 'cats eats' + str(total_cans) + ' cans.'
print(output)

output = '{} cats eats {} cans.'.format(cats, total_cans)
print(output)

output = f"{cats} cats eat {total_cans} cans."
print(output)

guests = ['Mary', 'Pete', 'David']
message = f"We are going to the cinema with my classmates: {', '.join(guests)} and me"
print(message)

message = 'We are going to the cinema with my classmates: {} and me'.format(', '.join(guests))
print(message)


import pandas as pd
