# Step 1: Word-Meaning Dictionary create karein
dictionary = {
    "Algorithm": "A step-by-step procedure or formula for solving a problem",
    "Variable": "A named storage location in memory that holds a value",
    "Function": "A block of organized, reusable code used to perform a single action",
    "Immutable": "An object whose state or value cannot be modified after creation",
    "Loop": "A sequence of instructions that is continually repeated until a certain condition is reached"
}
word = input("Enter a word to search its meaning: ").strip().capitalize()
meaning = dictionary.get(word, "Sorry, this word is not available in the dictionary")
print("\n--- Search Result ---")
print(f"Word   : {word}")
print(f"Meaning: {meaning}")