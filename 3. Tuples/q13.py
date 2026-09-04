names = ("Ishraq", "Khan", "Yousafzai", "Dua", "Arshad")

count = 0

for name in names:
    if len(name) > 5:
        count += 1

print(f"There are {count} names that have more than 5 letters.")