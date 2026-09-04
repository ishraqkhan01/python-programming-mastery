principle_amount=int(input("Enter priciple amount: "))
intrest_rate=float(input("Enter the annual intrest rate: "))
time=int(input("Enter time(money stays): "))

simple_intrest=principle_amount*intrest_rate*time/100
total_amount=simple_intrest+principle_amount

print(f"your intrest is: {simple_intrest}")
print(f"your total amount is: {total_amount}")
