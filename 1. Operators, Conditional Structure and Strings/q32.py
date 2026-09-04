total_bill_amount=int(input("Enter your total bill amount: "))
if total_bill_amount>=10000:
    discount_percentage=20
elif total_bill_amount>=5000 and total_bill_amount<=9999:
    discount_percentage=10
elif total_bill_amount>=2000 and total_bill_amount<=4999:
    discount_percentage=5
else:
    discount_percentage=0

discount_amount=(total_bill_amount * discount_percentage)/100
final_payable_amount=total_bill_amount-discount_amount
print("****************************************************")
print("**********bill calculator**********")
print(f"total bill amount: {total_bill_amount}")
print(f"dicount amout: {discount_amount}")
print(f"final payable amount: {final_payable_amount}")
print("****************************************************")