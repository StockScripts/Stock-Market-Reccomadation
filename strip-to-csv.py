import csv
import string

with open("TCS/TCS_data.csv") as f:
    reader = csv.reader(f, delimiter=",")
    with open("TCS/TCS.csv", "w") as fo:
        writer = csv.writer(fo)
        for rec in reader:
            writer.writerow(map(string.strip, rec))