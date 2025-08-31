"""
📌 CSV - (Comma-Separated Values)
    - Case sensitive
    - It’s a simple text file format used to store tabular data (like spreadsheets).
    - Each line is a row.
    - Each row has columns separated by commas.
    - used to store spreadsheets, simple databases, or tabular data.

    structure of .csv file      (Each next line → a record ; ( , ) separates values )
        name,age,city
        Dharmil,18,GJ01
        Nihar,18,GJ28
"""

# ------------------ CSV vs JSON -----------------
"""
| Aspect          | CSV                             | JSON                                    |
| --------------- | ------------------------------- | --------------------------------------- |
| Structure       | Tabular (rows & columns)        | Hierarchical (nested objects & arrays)  |
| Header          | Usually first row               | Keys in each object                     |
| Read in Python  | `csv.reader` / `csv.DictReader` | `json.load` / `json.loads`              |
| Write in Python | `csv.writer` / `csv.DictWriter` | `json.dump` / `json.dumps`              |
| Data types      | All text (numbers are strings)  | Maintains types (int, float, bool, etc) |
"""

# ------------------ Why CSV -----------------
"""
- CSV is plain text, so any program can read it: Excel, Google Sheets, Python, Java, even Notepad.
- Humans can open and read it easily.
- small in size
- Works with databases, Excel, data analysis libraries like pandas, and even web apps.
"""

"""
CSV:-
    - Data you want to open in Excel/Sheets easily
    - Flat structure → no nesting required
JSON:-
    - Nested objects, arrays, or key-value relationships
    - Data for web APIs, config files, or database records
    - Preserves types → numbers stay numbers, booleans stay booleans

CSV if the receiver expects spreadsheet-like data
JSON if the receiver is a web app or API

In short:
    - CSV = simple, flat, spreadsheet-friendly
    - JSON = complex, structured, API-friendly
"""

import csv

# ------------------ First write data in Data.csv ------------------

data = [
    ["Name", "Age", "City"],
    ["Sahil", 12, "Mumbai"],
    ["Mahi", 19, "Ahmedabad"]
]

with open("Data.csv", 'w') as cv:
    writer = csv.writer(cv)
    writer.writerows(data)
    # csv.writer(cv).writerows(data)

# ------------------ Read data from Data.csv ------------------

with open("Data.csv", 'r') as cv:
    reader = csv.reader(cv)
    for row in reader:
        print(row)

# All convert in text:-
# ['Name', 'Age', 'City']
# ['Sahil', '12', 'Mumbai']
# ['Mahi', '19', 'Ahmedabad']

# ------------------ Read as directory ------------------

with open("Data.csv", 'r') as cv:
    reader = csv.DictReader(cv)
    print(reader)               # <csv.DictReader object at 0x106ec42f0>
    print(reader.fieldnames)    # ['Name', 'Age', 'City']
    for row in reader:
        print(f"Row: {row}")    # Row: {'Name': 'Sahil', 'Age': '12', 'City': 'Mumbai'}
        print(f"Name is = {row['Name']}")

# ------------------ Add data ------------------

# Not recommended if structure change.
new = ["Ansh", 18, "Ahmedabad"]
with open("Data.csv", 'a') as cv:
    writer = csv.writer(cv)
    writer.writerow(new)

# Recommended
"""new1 = ["Dharmil",18,"Ahmedabad"]""" # This will not work
# case-sensitive
new = {'Name': 'Dharmil', 'Age': 18, 'City': 'Ahmedabad'}
with open("Data.csv", 'a') as cv:
    field = ["Name", "Age", "City"]
    writer = csv.DictWriter(cv, fieldnames=field)
    writer.writerow(new)

# List → csv.writer
# Dict → csv.DictWriter

# ------------------ Update data + delete ------------------

with open("Data.csv", 'r') as cv:
    reader = csv.DictReader(cv)
    row_delete = [row for row in reader if row['Age'] >= "18"]
print(row_delete)

with open('Data.csv', 'w') as f:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(row_delete)

students = []

# Read CSV first
with open('Data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Name'] == 'Dharmil':
            row['Age'] = '21'  # Update age
        students.append(row)

# Write back
with open('Data.csv', 'w') as f:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("Student age updated!")

# ------------------ Sort students ------------------

students = [
    {'Name': 'Dharmil', 'Age': '20', 'City': 'Ahmedabad'},
    {'Name': 'Nihar', 'Age': '18', 'City': 'Delhi'},
    {'Name': 'Ansh', 'Age': '19', 'City': 'Mumbai'}
]

students.sort(key=lambda x: int(x['Age']))  # sort by age
print(students)


# ------------------ SUMMARY ------------------
"""
- CSV (Comma-Separated Values) stores tabular data: rows separated by lines, columns by commas.
- CSV is case-sensitive and can be opened in Excel, Google Sheets, Python, or any text editor.
- Use csv.writer() / csv.writerows() to write lists, csv.DictWriter() to write dictionaries.
- Use csv.reader() to read rows as lists, csv.DictReader() to read rows as dictionaries with headers.
- Append rows using 'a' mode; update or delete requires reading all rows, modifying, and rewriting the file.
- Sorting can be done by reading into a list of dictionaries and using sort() with a key function.
- Recommended to use DictWriter/DictReader when headers are present to avoid mismatches.
- Keep headers consistent; convert data types manually if needed since CSV stores all values as strings.
"""
