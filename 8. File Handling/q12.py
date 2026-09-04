try:
    with open("data.txt","r",encoding="utd-8") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
else:
    print("Success! Data read perfectly.")