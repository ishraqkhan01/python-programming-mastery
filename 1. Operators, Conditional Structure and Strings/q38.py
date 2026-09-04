radius=float(input("Enter radius of a circle: "))
print("Press 1 for calculating area of a circle")
print("Press 2 for calculating circumference")
choice=int(input("Enter your choice: "))

if choice==1:
    area=(3.14159265359)*radius**2
    print(f"The area of circle is: {area}")
elif choice==2:
    circumference=2*(3.14159265359)*radius
    print(f"The circumference of a circle is: {circumference}")
else:
    print("Wrong choice! You can choose only 1 or 2")