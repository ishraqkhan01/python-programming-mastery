main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to search for: ")

if sub_string in main_string:
    print(f"Success: '{sub_string}' was found inside the main string.")
else:
    print(f"Failed: '{sub_string}' was not found inside the main string.")
