total_marks=100
obtained_marks=float(input("Enter your obtained marks(out of 100): "))

print("Press 1 for calculating percentage")
print("Press 2 for calculating Grade")
choice=int(input("Enter your choice: "))

if choice==1:
    percentage=(obtained_marks/total_marks)*100
    print(f"your percentage is: {percentage}")
elif choice==2:
    if obtained_marks>=95 and obtained_marks<=100:
      print("Grade: A++")
      print("Description: Exceptional")
      print("Grade Points: 5.0")
    elif obtained_marks>=90 and obtained_marks<=94.99:
      print("Grade: A+")
      print("Description: Outstanding")
      print("Grade Points: 4.7")
    elif obtained_marks>=85 and obtained_marks<=89.99:
      print("Grade: A")
      print("Description: Excellent")
      print("Grade Points: 4.3")
    elif obtained_marks>=80 and obtained_marks<=84.99:
      print("Grade: B++")
      print("Description: Very Good")
      print("Grade Points: 4.0")
    elif obtained_marks>=75 and obtained_marks<=79.99:
      print("Grade: B+")
      print("Description: Good")
      print("Grade Points: 3.7")
    elif obtained_marks>=70 and obtained_marks<=74.99:
      print("Grade: B")
      print("Description: Fairly Good")
      print("Grade Points: 3.3")
    elif obtained_marks>=60 and obtained_marks<=69.99:
      print("Grade: C")
      print("Description: Above Average")
      print("Grade Points: 3.0")
    elif obtained_marks>=50 and obtained_marks<=59.99:
      print("Grade: D")
      print("Description: Average")
      print("Grade Points: 2.7")
    elif obtained_marks>=40 and obtained_marks<=49.99:
      print("Grade: E")
      print("Description: Below Average")
      print("Grade Points: 2.3")
    else:
      print("Grade: U")
      print("Description: Unsatisfactory")
      print("Grade Points: 0.0")
else:
  print("Wrong Choice!")
    
    