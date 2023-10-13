# Make a program that asks a password.

correct_password = "secretpassword"

user_password = input("Enter the password: ")

if user_password == correct_password:
    print("Access granted. Welcome!")
else:
    print("Access denied. Incorrect password.")