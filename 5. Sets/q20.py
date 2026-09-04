numbers_set = {10, 20, 30, 40, 50}
print(f"Initial set: {numbers_set}")

is_present = 30 in numbers_set
print(f"Is 30 present in set? : {is_present}")

numbers_set.add(60)
print(f"After adding 60    : {numbers_set}")

numbers_set.discard(20)
print(f"After removing 20  : {numbers_set}")

total_elements = len(numbers_set)
print(f"Total unique items : {total_elements}")