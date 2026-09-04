file=open("Plnames.txt","r",encoding="utf-8")
content=file.readlines()
print(content)
for i in content:
    print(i,end='')

file.close()