total_seconds=int(input("Enter total number of seconds: "))
print("Press 1 for seconds to hour")
print("Press 2 for seconds to minutes")
choice=int(input("Enter your choice: "))

if choice==1:
    hour=int(total_seconds/3600)
    print(f"total number of hour is: {hour:.2f}")
elif choice==2:
    minutes=total_seconds/60
    print(f"total number of mintues is: {minutes:.2f}")
else:
    print("Wrong choice!")