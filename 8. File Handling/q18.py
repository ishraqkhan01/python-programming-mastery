import json

student_data = {
    "name": "Ishraq Khan",
    "age": 21,
    "city": "Peshawar",
    "skills": ["Python", "Data Analysis", "SQL", "Git"]
}

with open("student_info.json", "w", encoding="utf-8") as file:
    json.dump(student_data, file, indent=4)

print("Data successfully saved to student_info.json!\n")


with open("student_info.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print("--- Loaded Data ---")
print(loaded_data)