import csv

data = [
    ["Name", "Age", "Marks"],
    ["Ishraq", "20", "92"],
    ["Khan", "21", "85"],
    ["Yousafzai", "22", "88"]
]

with open("stdrecord.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data successfully written to file!\n")

with open("stdrecord.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)