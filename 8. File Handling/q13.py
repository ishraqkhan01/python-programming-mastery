with open("numbers.txt","r",encoding="utf-8") as file:
    for i in file:
        sqr=int(i)**2
        print(sqr)