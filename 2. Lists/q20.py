numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input("Enter number you wanna search: "))

if num in numbers:
    print(f"Found! {num} exists at index {numbers.index(num)}")
else:
    print(f"Not Found! {num} does not exist in the list")