

def age_validated(age):
    if type(age) != int:
        raise Exception("Age must be an integer")

    if age < 0:
        raise ValueError("Only positive integers are allowed")

    assert 12 < age <= 19

    return True

def name_validated(name):
    if ',' not in name:
        raise ValueError("Incorrect input: Minning ',' to sepparate name and surname")

    first_name, surname = name.split(',')

    if not len(first_name) or not len(surname):
        raise ValueError("Incorrect input: Missing name or surname value")

    return True

# print(age_validated(17))
# print(age_validated(20))
# print(age_validated('18'))
# print(name_validated("fatma,el"))
# print(name_validated("fatma"))
# print(name_validated("fatma,"))

is_succesful = True

try:
    name = input("Please enter your name separeted by comma:")
    name_validated(name)

    age = int(input("Enter your age: "))
    age_validated(age)

except ValueError as e:
    print(f"Invalid input: {str(e)}")

except AssertionError as e:
    print(f"Error - {str(e)}: The age is not within the teen category!")

else:
    with open("registration_file.txt", "a+") as file:
        file.write(f"New member name: {name} and age {age}. \n")
    is_succesful = True

finally:
    if is_succesful:
        print("Registration process completed Succesfully!")
    else:
        print("Could not complet registration. Please try again")