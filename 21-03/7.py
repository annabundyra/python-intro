

def readFile(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.readlines())

    except FileNotFoundError as e:
        print(f"Error: {e}")

readFile("registration_file.txt")