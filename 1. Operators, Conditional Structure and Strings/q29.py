phone_no=input("Enter Your Phone no(must be 11 digit): ")

if len(phone_no)>11 or len(phone_no)<11:
    print("Phone no must be 11 digits")
else:
    last_four_digit=phone_no[-4:]
    mask_count=len(phone_no)-4
    masked_part="*"*mask_count
    final_combine=masked_part+last_four_digit
    print(final_combine)  

 

