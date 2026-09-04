subject_marks={
    "mathematics": 98,
    "bilogy":85,
    "english":76,
    "islamiat":41,
    "pakstudy":35,
    "physcics":90,
    "urdu":95
}

for key,val in subject_marks.items():
    if val >=80:
        print(f"{key} : {val}")