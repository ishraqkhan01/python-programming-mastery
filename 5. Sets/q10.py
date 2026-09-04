set_a=set([1,2,3,4])
set_b=set([5,6,7,8])

print("Union using Union(): ")
union_a=set_a.union(set_b)
print(union_a)

print("Union using |: ")
union_b=set_a | set_b
print(union_b)