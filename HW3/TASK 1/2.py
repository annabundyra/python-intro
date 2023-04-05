




my_money = input('How much money do you have? ')
hour = 3
venue_cost = (200*hour) * 1.1
if int(my_money) >= venue_cost:
  print('You can afford the venue')
else:
  print('You cannot afford the venue')