sentence=input("Enter a sentence: ")
word=input("Enter a word you want to search: ")

if word in sentence:
    print("Word Found")
else:
    print("Word not found")