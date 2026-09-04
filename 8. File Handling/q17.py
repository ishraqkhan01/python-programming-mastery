import csv
with open('stdrecord.csv', mode='r', newline='', encoding='utf-8') as file:
    dict_reader = csv.DictReader(file)
    for row in dict_reader:
        print(row['Name'], row['Age'], row['Marks'])