import csv

with open("election_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # skips the headers and goes to the first value in the set
    next(csv_reader)

    for line in csv_reader:
        print(line)
