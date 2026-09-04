student_names=["Ishraq", "Khan", "Yousafzai", "Dua", "Arshad"]
second_student=student_names[1]
second_last_student=student_names[-2]
total_student=len(student_names)
last_item_index = student_names.index(student_names[-1])
total_indexing = last_item_index + 1

print(f"The second student name: {second_student}")
print(f"The second last: {second_last_student}")
print(f"Total Students using len: {len(student_names)}")
print(f"Total students using indexing: {total_indexing}")