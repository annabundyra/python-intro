
name = input("What is your name? ")
is_admin = name == 'admin'

password = input("What is your password? ")
is_password = password = 'dinos'

if(is_admin and is_password):
    print("Welcome! ")
elif(is_admin or is_password):
    print("Try again!")
else:
    print("Go away!")