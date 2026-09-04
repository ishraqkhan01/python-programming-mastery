set_a=set([1,2,3,4,5])
set_b=set([3,4,5,6,7])

print("Intersection using Intersection(): ")
intersection_a=set_a.intersection(set_b)
print(intersection_a)

print("Intersection using &: ")
intersection_b=set_a & set_b
print(intersection_b)