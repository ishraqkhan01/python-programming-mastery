width=float(input("Enter width of a rectangle: "))
length=float(input("Enter length of a rectangle: "))

print("Press 1 for calculating the area of a rectangle: ")
print("Press 2 for calculating the perimeter of a rectangle: ")
choice=int(input("Enter your choice: "))

if choice==1:
    area=length*width
    print(f"The Area of a rectangle is: {area}")
elif choice==2:
    perimeter=2*(length+width)
    print(f"The perimeter of a rectangle is: {perimeter}")
else:
    print("Wrong choice! You can only 1 or 2")
