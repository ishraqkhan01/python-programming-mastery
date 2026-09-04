list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"Memory ID of list1: {id(list1)}")
print(f"Memory ID of list2: {id(list2)}")
print(f"Memory ID of list3: {id(list3)}")

print(f"list1 is list2: {list1 is list2}") 
print(f"list1 is list3: {list1 is list3}")

print(f"list1 is not list2: {list1 is not list2}")  
print(f"list1 is not list3: {list1 is not list3}") 