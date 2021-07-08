import csv

results = []

with open("orders.csv") as File:
    reader = csv.reader(File)
    print(reader)
    for row in reader:
        # results.append(row)
        print("Products: {0}".format(row[2]))
    # print(results)
