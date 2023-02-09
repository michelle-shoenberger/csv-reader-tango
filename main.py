import csv 

def animal():
    an = input("Choose cats or dogs: ")
    with open(f"./data/{an}.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        counter = 0
        for row in reader:
            if counter == 0:
                counter += 1
                continue
            print(f"{row[0]} is a{row[1]} year{'s' if int(row[1])>1 else ''} old{row[2]}")

animal()