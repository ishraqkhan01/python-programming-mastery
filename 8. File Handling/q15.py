import os

with open("old_name.txt", "w", encoding="utf-8") as file:
    file.write("Hello, this is a test message!")

os.rename("old_name.txt", "new_name.txt")

if os.path.exists("new_name.txt"):
    print("Success: 'new_name.txt' successfully created and renamed!")
    
    with open("new_name.txt", "r", encoding="utf-8") as file:
        print("File Content:", file.read())