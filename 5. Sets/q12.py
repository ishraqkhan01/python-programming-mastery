set_a=set([1,2,3,4,5])
set_b=set([3,4,5,6,7])

print("Difference using Difference(): ")
difference_a=set_a.difference(set_b)
print(difference_a)

print("Difference using -: ")
difference_b=set_a - set_b
print(difference_b)