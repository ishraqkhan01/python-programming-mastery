file=open("stdnames.txt","r",encoding="utf-8")
for i in range(0,3):
    print(file.readline(),end='')

file.close()