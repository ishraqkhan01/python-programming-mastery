with open("sentence.txt","r",encoding="utf-8") as file:
    chuck=file.read(7)
    print(chuck)
    print(f"The current cursor location in the file are: {file.tell()}")
    file.seek(0)
    print(file.read())
