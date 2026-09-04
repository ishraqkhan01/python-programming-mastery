numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
def process_numbers(numbers):
    even_count=0
    odd_count=0
    for i in numbers:
        if i%2==0:
            even_count=even_count+1
        else:
            odd_count=odd_count+1
    return even_count,odd_count

total_even,total_odd=process_numbers(numbers)
print(f"Total Even numbers is: {total_even}")
print(f"Total Odd Numbers is: {total_odd}")