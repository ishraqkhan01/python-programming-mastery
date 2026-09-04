student={
    "name":"Ishraq Khan",
    "age":23,
    "department":"Computer Science",
    "CGPA":3.8
}

print(f"before pop: {student}")
pop_val=student.pop("name")
print(f"the pop value is: {pop_val}")
print(f"the updated dictionary is: {student}")
