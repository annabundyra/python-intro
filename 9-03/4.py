

#for number in range(5):
#   print(number)

total = 0
for number in range (3):

    print("Total value is: " + str(total))
    print("This is run No" + str(number + 1) + "inside the loop\n")
    total = total + 10

print("\nWe are outside the loop now")
print("The final result is {}".format(total))