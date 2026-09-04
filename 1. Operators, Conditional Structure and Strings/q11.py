# Grading System for Matric and Fsc
marks=float(input("Enter Your Marks: "))

if marks>=95 and marks<=100:
    print("Grade: A++")
    print("Description: Exceptional")
    print("Grade Points: 5.0")
elif marks>=90 and marks<=94.99:
    print("Grade: A+")
    print("Description: Outstanding")
    print("Grade Points: 4.7")
elif marks>=85 and marks<=89.99:
    print("Grade: A")
    print("Description: Excellent")
    print("Grade Points: 4.3")
elif marks>=80 and marks<=84.99:
    print("Grade: B++")
    print("Description: Very Good")
    print("Grade Points: 4.0")
elif marks>=75 and marks<=79.99:
    print("Grade: B+")
    print("Description: Good")
    print("Grade Points: 3.7")
elif marks>=70 and marks<=74.99:
    print("Grade: B")
    print("Description: Fairly Good")
    print("Grade Points: 3.3")
elif marks>=60 and marks<=69.99:
    print("Grade: C")
    print("Description: Above Average")
    print("Grade Points: 3.0")
elif marks>=50 and marks<=59.99:
    print("Grade: D")
    print("Description: Average")
    print("Grade Points: 2.7")
elif marks>=40 and marks<=49.99:
    print("Grade: E")
    print("Description: Below Average")
    print("Grade Points: 2.3")
else:
    print("Grade: U")
    print("Description: Unsatisfactory")
    print("Grade Points: 0.0")