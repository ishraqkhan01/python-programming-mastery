my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
number = int(input("Enter a number: "))

found = False
counter = 0 

for i in my_list:
    if i == number:
        found = True
        break 
    counter += 1 

if found:
    print(f"The number {number} is found at index {counter}")
else:
    print(f"The number {number} was not found in the list")