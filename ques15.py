import csv

# Specify the CSV file name
file_name = "data.csv"

# Read data from the CSV file
with open(file_name, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(', '.join(row))
