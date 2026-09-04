file=open("aboutpy.txt","r",encoding="utf-8")
content1=file.read(10)
print(content1)

print(file.read())

file.close()