principle_amount=int(input("Enter priciple amount: "))
intrest_rate=float(input("Enter the annual intrest rate: "))
time=int(input("Enter time(money stays): "))

total_amount=principle_amount*((1+intrest_rate/100)**time)
compound_interest=total_amount-principle_amount

print(f"your compound intrest is: {compound_interest}")