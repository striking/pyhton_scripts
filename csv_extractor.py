import csv

with open('aus-tilers-yellowpages.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[1])

f.close()