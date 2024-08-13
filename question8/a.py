import csv

fields = ['name', 'class', 'year', 'course']
rows = [['souro', 'A', '2022', 'B.Tech'],['hope', 'AX', '20xx', 'UNKNOWN']]

with open('student_d.csv','w',newline='') as f:
    writer_cursor = csv.writer(f)
    writer_cursor.writerow(fields)
    writer_cursor.writerows(rows)