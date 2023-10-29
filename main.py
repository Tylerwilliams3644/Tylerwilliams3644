import csv

with open("budget_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        profit_loss = line[1]
        # dates = line[0]
        # print(profit_loss)
        # print(dates)
        # sum_profit_loss = sum(int(profit_loss))
        # print(int(sum_profit_loss))
        # print(int(profit_loss))
        # print(profit_loss)
