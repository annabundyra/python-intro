
denominator = int(input("Please enter a number to divide by:"))

try:
    division_result = 100 / int(denominator)
    print(division_result)

except Exception as e:
    print(f"Error: {str(e)}")

