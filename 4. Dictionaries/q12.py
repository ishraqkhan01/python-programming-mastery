student_firstinfo={
    "name":"Ishraq Khan",
    "age":22,
    "department":"Computer Science",
    "University":"CUST",
}

print(student_firstinfo)
student_secondinfo={
     "Passing Year": 2026,
     "Earned Credit hour":130
}
print(student_secondinfo)

student_firstinfo.update(student_secondinfo)
print(student_firstinfo)