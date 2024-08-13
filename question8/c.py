# Import csv library
import csv
 
# Open "employees.csv"  file on append mode ("a")
# It means the line that will be added will go to the last row.
with open("student_d.csv", "a") as infile:
    # Create a writer object for csv
    writer = csv.writer(infile)
    # Data we want to write to the CSV file
    line = ["pope", "X", "2023", "CSE"]
    # Write the row the CSV file.
    # Note that this line updates the file in-place
    writer.writerow(line)