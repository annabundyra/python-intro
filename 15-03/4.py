import csv

field_names = ['name', 'age']
data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28}
]

with open('team.csv', 'w+') as csv_file:
    spreadcheet = csv.DictWriter(csv_file, fieldnames = field_names)

    spreadcheet.writeheader()
    spreadcheet.writerows(data)

with open('team.csv', 'r') as csv_file:
    spreadcheet = csv.DictReader(csv_file)
    print(type(spreadcheet))
    for row in spreadcheet:
        print(dict(row))