while True:
    print("\n--- Student Record Manager ---")
    print("Press 1 for adding student record")
    print("Press 2 for Reading/Displaying record")
    print("Press 3 for Exit")
    
    try:
        choice = int(input("Enter your choice = "))
    except ValueError:
        print("Invalid input! Please enter a number (1, 2, or 3).")
        continue

    if choice == 1:
        name = input("Enter name = ")
        age = input("Enter age = ")
        marks = input("Enter marks (out of 100) = ")
        
        with open("STD.txt", "a", encoding="utf-8") as file:
            file.write(f"Name: {name} | Age: {age} | Marks: {marks}\n")
            
        print(f"Record for '{name}' successfully added into the file!")

    elif choice == 2:
        try:
            with open("STD.txt", "r", encoding="utf-8") as file:
                content = file.read()
                
                if not content.strip():
                    print("File is empty, nothing to print!")
                else:
                    print("\n--- Saved Student Records ---")
                    print(content)
                    
        except FileNotFoundError:
            print("Error: 'STD.txt' file does not exist yet! Add a record first.")

    elif choice == 3:
        print("Exiting program... Goodluck!")
        break
        
    else:
        print("Wrong choice! Please enter 1, 2, or 3.")