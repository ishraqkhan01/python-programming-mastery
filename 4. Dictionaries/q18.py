employees={
    "Ishraq Khan":200000,
    "Dua Arshad":150000,
    "Nouman":140000,
    "Moniza Shahid":135000,
    "Sahil Jamal":130000
}

count=0
for key,val in employees.items():
    if val>100000:
        count=count+1
    else:
        pass
print(f"there are {count} employees whose salary is more then 100,000")