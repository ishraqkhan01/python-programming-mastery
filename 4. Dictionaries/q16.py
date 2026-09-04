mapping = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

num = int(input("Enter a number: "))
if num in mapping:
    print(f"Matching word: {mapping[num]}")
else:
    print("Invalid input! Number not found in mapping.")