print("--------------- salary bonus calculator ---------------")
current_salary=int(input("Enter your current salary: "))
performence_score=int(input("Enter your performence score(1 to 5): "))

if performence_score==5:
    bonus_percentage=20
elif performence_score==4:
    bonus_percentage=10
elif performence_score==3:
    bonus_percentage=5
else:
    bonus_percentage=0

bonus_amount=(current_salary*bonus_percentage)/100
bonus_salary=current_salary+bonus_amount

print(f"Salary: {current_salary}")
print(f"Bonus Percentage: {bonus_percentage}")
print(f"Bonus Amount: {bonus_amount}")
print(f"Bonus Salary: {bonus_salary}")
