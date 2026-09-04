password = input("Enter your password: ")

is_long_enough = len(password) >= 8
has_no_spaces = " " not in password
has_mixed_case = not password.islower() and not password.isupper()
has_special_char = not password.isalnum()

if is_long_enough and has_no_spaces and has_mixed_case and has_special_char:
    print("Password is valid!")
else:
    print("Password is invalid. It must be at least 8 characters, contain no spaces, and include a mix of uppercase, lowercase, and special characters.")