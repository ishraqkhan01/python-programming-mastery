string=input("Enter a String: ").lower()
reverse=string[::-1]

if string==reverse:
    print(f"The sting {string} is palindrome")
else:
    print(f"The sting {string} is not palindrome")