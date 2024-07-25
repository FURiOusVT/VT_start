import csv

data = [["Star Wars", "Terminator", "A I"],["Fool", "Mathilda", "Leviathan"],
        ["Men in black", "I am robot", "Evolution"]]

with open('series_list.csv', 'w', newline = '') as a:
    b = csv.writer(a, delimiter=",")
    for item in data:
        b.writerow([item])
