subject_marks={
    "mathematics": 98,
    "bilogy":85,
    "english":76,
    "islamiat":41,
    "pakstudy":35,
    "physcics":90,
    "urdu":95
}

marks_sum=0
for vals in subject_marks.values():
    marks_sum+=vals

avg=marks_sum/len(subject_marks)
print(f"total obtained marks: {marks_sum}")
print(f"averge: {avg:.2f}")
