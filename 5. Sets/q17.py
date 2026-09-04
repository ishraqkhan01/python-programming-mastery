set_of_number=set([1,2,3,4,5,6,7,8,9,0])
for i in set_of_number:
    print(i)

num=int(input("Enter a number: "))
if num in set_of_number:
    print("Number Exists")
else:
    print("Not Exists")