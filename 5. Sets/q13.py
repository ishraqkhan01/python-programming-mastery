set_a=set([1,2,3,4,5])
set_b=set([3,4,5,6,7])

print("Symmetric Difference using symmetric_difference(): ")
symmetric_difference_a=set_a.symmetric_difference(set_b)
print(symmetric_difference_a)

print("Symmetric Difference using ^: ")
symmetric_difference_b=set_a ^ set_b
print(symmetric_difference_b)