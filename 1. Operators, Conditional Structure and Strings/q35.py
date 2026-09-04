print("------------- celsius to fahrenheit / fahrenheit to celsius -------------")
print("Press 1 for celsius to fahrenheit")
print("Press 2 for fahrenheit to celsius")
choice=int(input("Enter your choice: "))
if choice==1:
    celsius=float(input("Enter celsius: "))
    fahrenheit=(celsius*1.8)+32
    print(f"Fahrenheit: {fahrenheit}°F")
elif choice==2:
    fahrenheit=float(input("Enter fahrenheit: "))
    celsius=(fahrenheit-32) * 5/9
    print(f"Celsius: {celsius}°C")
else:
    print("Wrong choice! you can chose only 1 or 2")
