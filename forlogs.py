import csv

costlist = []

with open ('dogslogs1.tsv', newline="") as file:
    reader = csv.reader(file, delimiter='	')
    for row in reader:
       costlist.append(int(row[3]))

costlist.insert(0, 0)

maxcost = max(costlist)

with open ('dogslogs.tsv', newline="") as file:
    reader = csv.DictReader(file, delimiter='	')
    for row in reader:
        data = row
        for item in data:
            if str(maxcost) in data[item]:
                print (row)

