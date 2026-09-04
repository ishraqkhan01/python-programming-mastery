def calculate_sum(*numbers):
    Sum=0
    for i in numbers:
        Sum=Sum+i
    return Sum

print(f"The Sum is: {calculate_sum(1,2)}")
print(f"The Sum is: {calculate_sum(1,2,3,4,5)}")
print(f"The Sum is: {calculate_sum()}")

