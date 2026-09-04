correct_password = "@Eie2026"
user_input = input("Enter password: ")

while user_input != correct_password:
    print("Incorrect password! Try again.")
    user_input = input("Enter password: ")

print("Access Granted! Welcome.")