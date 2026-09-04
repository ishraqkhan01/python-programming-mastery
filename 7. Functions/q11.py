def count_vowels(text):
    count=0
    vowels="aeiou"

    for char in text.lower():
        if char in vowels:
            count+=1
    return count

print(f"Total number of vowels is: {count_vowels("Ishraq Khan")}")
print(f"Total number of vowels is: {count_vowels("Dua Arshad")}")
print(f"Total number of vowels is: {count_vowels("Hamza Sohail")}")



