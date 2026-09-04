str1=input("Enter a string: ").lower()
count=0
for i in str1:
    if i=="a":
        count=count+1
    elif i=="e":
        count=count+1
    elif i=="i":
        count=count+1
    elif i=="o":
        count=count+1
    elif i=="u":
        count=count+1
    else:
        pass

print("Total number of vowels appears in a string is:",count)