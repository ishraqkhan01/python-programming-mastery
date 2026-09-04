def calculate_rectangle(length, width):
    Area_of_rectangle=length*width
    Parimeter_of_rectangle=2*(length+width)
    return Area_of_rectangle,Parimeter_of_rectangle

Area, Perimeter=calculate_rectangle(2,4)
print(f"Area of a rectangle: {Area}")
print(f"Parimete of a rectangle: {Perimeter}")