"""
 📌 Json -> Csv
"""

import csv
import json

# JSON data
data = [
    {"name": "Dharmil", "age": 21, "city": "Ahmedabad"},
    {"name": "Rahul", "age": 22, "city": "Mumbai"},
    {"name": "Sneha", "age": 20, "city": "Delhi"}
]

# If in other .json file
# with open(json_file, 'r') as jf:
#         data = json.load(jf)

# Convert JSON to CSV
with open('data.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()  # write column names
    writer.writerows(data)  # write all rows

"""
 📌 Csv -> Json
"""

# Read CSV and convert to JSON
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data_list = list(reader)

# Optional: Convert string numbers to int
for item in data_list:
    item['age'] = int(item['age'])

# Save JSON
with open('data.json', 'w') as json_file:
    json.dump(data_list, json_file, indent=4)

"""
1. JSON to CSV
    JSON is usually a list of dictionaries.
    Use Python’s csv.DictWriter to write dictionaries as CSV rows.
    Steps:
        - Open JSON file and load data using json.load().
        - Open CSV file in write mode.
        - Create csv.DictWriter(file, fieldnames=data[0].keys()).
        - Write header with writer.writeheader().
        - Write rows with writer.writerows(data).

2. CSV to JSON
    CSV stores data in rows with headers.
    Use csv.DictReader to read CSV into dictionaries.
    Steps:
        - Open CSV file and read rows with csv.DictReader().
        - Convert numeric strings to int or float if needed.
        - Save data as JSON using json.dump(data_list, file, indent=4).
"""
