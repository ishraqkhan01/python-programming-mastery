def find_largest(numbers):
    max=numbers[0]
    for i in numbers:
        if i > max:
            max=i

    return max


print(f"The Largest number in a list is: {find_largest([10,20,30,40,50])}")