words=("Ishraq", "Khan", "Yousafzai", "Dua", "Arshad")
word=input("Enter a word: ").title()
if word in words:
    print(f"the word {word} is exist")
else:
    print(f"the word {word} is not exist")