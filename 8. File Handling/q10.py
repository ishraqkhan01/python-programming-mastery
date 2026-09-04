with open("multilingual.txt", "w", encoding="utf-8") as file:
    file.write("Hello World!\n")
    file.write("پائتھون ایک بہترین زبان ہے (Python is awesome!)\n")
    file.write("Bonjour, comment ça va?\n")

with open("multilingual.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)