num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))

print("*******************************")
print("Press 1 for Addition (+)")
print("Press 2 for Subtraction (-)")
print("Press 3 for Multiplication (*)")
print("Press 4 for Division (/)")
print("Press 5 for Floor Division (//)")
print("Press 6 for Modulus (%)")
print("Press 7 for Exponentiation (**)")
choice=int(input(""))
print("*******************************")

if choice==1:
    Sum=num1+num2
    print(f'The Sum of {num1} and {num2} is: {Sum}')
elif choice==2:
    Sub=num1-num2
    print(f'The Subtraction of {num1} and {num2} is: {Sub}')
elif choice==3:
    Mul=num1*num2
    print(f'The Multiplication of {num1} and {num2} is: {Mul}')
elif choice==4:
    Div=num1/num2
    print(f'The Division of {num1} and {num2} is: {Div}')
elif choice==5:
    Floor_Div=num1//num2
    print(f'The Floor Divison of {num1} and {num2} is: {Floor_Div}')
elif choice==6:
    Mod=num1%num2
    print(f'The Mudulus of {num1} and {num2} is: {Mod}')
else:
    Exp=num1**num2
    print(f'The Exponentiation of {num1} and {num2} is: {Exp}')


