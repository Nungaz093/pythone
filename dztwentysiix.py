import csv

data = [
    ['hostname', 'vendor', 'model', 'location'],
    ['sw1', 'Cisco', '3750', 'London'],
    ['sw2', 'Cisco', '3850', 'Liverpool'],
    ['sw3', 'Cisco', '3650', 'Liverpool'],
    ['sw4', 'Cisco', '3650', 'London']
]

with open("dz20.csv", "w") as f:
    writer = csv.writer(f, delimiter=";", lineterminator="\r")
    for row in data:
        writer.writerow(row)

