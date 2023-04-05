

denominator = int(input("Please enter a number to divide by:"))

try:
    try:
        division_result = 100 / int(denominator)
        print(division_result)
    except ValueError:
        print("Valer error")
        
except ZeroDivisionError:
    print("You cannot divide by 0, try again")