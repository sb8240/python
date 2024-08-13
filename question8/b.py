import csv

with open('student_d.csv', 'r',newline='') as f:
    reading = csv.reader(f)
    
    for row in reading:
        print(row)