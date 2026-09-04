list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
for i in list1:
    if i%2==0:
        list2.append(i)
    else:
        pass

print(f"list 1: {list1}")
print(f"list 2: {list2}")