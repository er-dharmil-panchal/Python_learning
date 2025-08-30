"""
📌 JSON (JavaScript Object Notation)
    - .json extension
"""

# ------------------ What is JSON ? ------------------
"""
    - It’s a way to store and exchange data
    - It's just text data written in a structured format: (keys, values)
    - Your names, symbols, or emojis are saved safely (UTF-8)
"""

# ------------------ Why JSON ? ------------------
"""
Before JSON
    - Random plain text → messy, inconsistent, hard for programs to parse.
    - XML → structured, but bulky and hard to work with.

With JSON
    - Lightweight (less space)
    - structured (have some strict rule)
    - Universal
    - Readable by humans and computers
    - Perfect for APIs and databases

    • JSON is the industry standard for data exchange, used in APIs, configs, and databases.
"""

# ------------------ Rules of JSON (strict) ------------------
"""
    - JSON is case-sensitive
    - Data is written in key–value pairs
    - Keys must be in double quotes ('age':20 ❌.. "age":20 ✅)
    - The whole data is wrapped in curly braces {} for objects
    - Lists (arrays) are in square brackets [] ( e.g. "skills": ["Python", "Java"] )
"""

# ------------------ Some value rules ------------------
"""
    - String → "text" (must be in double quotes)
    - Number → 20 (no quotes)
    - Boolean → true or false (lowercase)
    - Null → null
    - Array → ["Python", "Java"]
    - Object → { "city": "Ahmedabad" }
    - Spaces, tabs, or line breaks are only for humans to read better.

NOTE :- JSON ignore extra space (Spaces, tabs, or line breaks are only for humans to read better.)
    - {"Name" : "Dharmil"}

    - {
          "Name" : "Dharmil"
      }
"""

# ------------------ Example of valid JSON ------------------
valid_json_example = """
{
  "name": "Dharmil",
  "age": 20,
  "is_student": true,
  "skills": ["Python", "Java", "SQL"],
  "address": {
    "city": "Ahmedabad",
    "pin": 380001
  },
  "nickname": null
}
"""

# ------------------ Example of invalid JSON ------------------
invalid_json_example = """
{
  name: Dharmil,   // ❌ keys need double quotes
  "age": "20",     // ✔ valid but treated as a string, not a number
  "skills": ["Python", "Java",] // ❌ trailing comma
}
"""

# NOTE :- Dictionary in python are same, but it works only inside python
#        but json can work for java,js,python, and even work to store data in database

import json

data = {
    "name": "Dharmil",
    "age": 18,
    "is_student": True,
    "skills": ["Python", "Java", "SQL"],
    "address": {
        "city": "Ahmedabad",
        "pin": 382481
    }
}

"""
json.dump() :- Write data to a file
json.dumps() :- Convert to JSON string (not file)
json.load() :- Read JSON from a file
json.loads() :- Convert JSON string → Python object
"""

# ------------------ Convert to JSON string ------------------
json_str = json.dumps(data)
print(json_str)

# Pretty print in JSON
json_string = json.dumps(data, indent=4)
print(json_string)

# ------------------ Saving data in First.json ------------------
with open("First.json", 'w') as f:
    f.write(json_string)

# ------------------ Reading from First.json ------------------
with open("First.json", 'r') as f:
    data1 = json.load(f)            # load not loads ,, it returns file not string
    print(data1)
    print(type(data1))              # dict

# ------------------ Fetch data from JSON string ------------------
data_text = '{"name": "Dharmil","age": 18, "is_student": true,"skills": ["Python", "Java", "SQL"],"address": {"city": "Ahmedabad","pin": 382481}}'

# NOTE:- Remember when we write boolean in python True, False same for Null
# -> when we write this data in .json it will automatically convert into true,false
# -> but when we do like this with text we have to do true
data2 = json.loads(data_text)
print(data2["name"])

# ---->> Better option :- read from json file
# Makes it easy to update data without editing Python code.
# Perfect for configs, APIs, or saving program output.
with open("First.json", 'r') as f:
    data_json = json.load(f)

print(f"Name :- {data_json['name']}")
print(f"Age :- {data_json['age']}")
print(f"Is student ? :- {data_json['is_student']}")
print(f"Skills :- {data_json['skills']}")

# ------------------ Update JSON ------------------
with open("First.json", 'r') as f:
    data = json.load(f)

# when we dump (not dumps) we have to also give the object of file in argument.
data["Gender"] = "Male"                  # Add new data
data["address"]["city"] = "Surat"        # can change in nested data particulate values
data["address"]["pin"] = 380001
data["skills"].append("HTML")            # can add new in list items
with open("First.json", 'w') as f:
    json.dump(data, f, indent=4)

# ------------------ Example: Python list of dictionaries (objects) ------------------
users = [
    {
        "id": 1,
        "name": "Dharmil",
        "skills": ["Python", "Java"],
        "is_student": True
    },
    {
        "id": 2,
        "name": "Raj",
        "skills": ["C++", "SQL"],
        "is_student": False
    },
    {
        "id": 3,
        "name": "Neha",
        "skills": ["JavaScript", "React"],
        "is_student": True
    }
]

# storing data in .json
with open("User.json", 'w') as f:
    json.dump(users, f, indent=4)

# reading data from .json
with open("User.json", 'r') as f:
    data = json.load(f)

print(type(data))       # list, because there is multiple objects data
for users in data:
    print("===================================")
    print(f"name - {users['name']}")
    print(f"id - {users['id']}")
    print(f"skills - {users['skills']}")

# ------------------ Adding new user ------------------
new_user = '{"id" : 4, "name" : "Nihar", "skills":["Java","Python"], "is_student": false}'
new_user_dict = json.loads(new_user)  # Convert JSON string to Python dict to ensure correct JSON format and proper data types
data.append(new_user_dict)             # Append the validated dictionary to the existing list of users

# ✅✅ NOTE: IMPORTANT - You *could* do data.append(new_user) directly,
# but it's not recommended. Doing so may cause issues if the new JSON string
# does not match the structure or data types of the existing list.
# Converting it first with json.loads() ensures correct format and safe appending.

# ------------------ Handling non-ASCII characters ------------------
data = {
    "name": "Dharmil",
    "city": "Ahmedabad",
    "emoji": "😊",
    "language": "हिन्दी"
}

# Default behavior (ensure_ascii=True)
json_str = json.dumps(data)
print(json_str)         # {"name": "Dharmil", "city": "Ahmedabad", "emoji": "\ud83d\ude0a", "language": "\u0939\u093f\u0928\u094d\u0926\u0940"}

json_str = json.dumps(data, ensure_ascii=False)
print(json_str)         # {"name": "Dharmil", "city": "Ahmedabad", "emoji": "😊", "language": "हिन्दी"}

# ------------------ Handling JSON Exceptions in Python ------------------
"""
1️⃣ json.JSONDecodeError
    - Raised when the JSON string/file has invalid syntax.
    - Causes:
        • Missing comma, quote, or bracket
        • Malformed JSON content
    - Always check your JSON format before loading.

2️⃣ FileNotFoundError
    - Occurs if the JSON file you are trying to open does not exist.

3️⃣ PermissionError
    - Happens when you don't have permission to read or write the file.

4️⃣ TypeError
    - Raised while dumping (writing) unsupported Python objects to JSON.
    - Example:
        • Writing a Python set
        • Writing a custom class object without conversion

5️⃣ UnicodeEncodeError / UnicodeDecodeError
    - Triggered when encoding or decoding special characters fails.
    - Often fixed by using UTF-8 encoding when opening the file.

6️⃣ ValueError (Legacy)
    - Older Python versions (<3.5) used ValueError instead of JSONDecodeError
      for invalid JSON syntax.

✅ Best Practices:
• Always use try-except blocks for JSON operations.
• Validate JSON structure before loading.
• Open files with encoding="utf-8" to avoid Unicode issues.
• Convert custom objects (like classes) to dictionaries before dumping.
• Keep backups of important JSON files to prevent accidental corruption.
"""

# ------------------ Nested JSON helper ------------------
def get_nested(data, keys):
    for key in keys:
        data = data.get(key, {})  # if key doesnt exist then it will return {}
    return data

nested_data = {
    "user": {"profile": {"name": "Dharmil", "city": "Ahmedabad"}}
}

print(get_nested(nested_data, ["user", "profile", "name"]))  # Dharmil

# ------------------ Convert custom class to JSON ------------------
class student:
    def __init__(self, name, age, boolean):
        self.name = name
        self.age = age
        self.boolean = boolean

s1 = student("Mohan", 18, True)
json_txt = json.dumps(s1.__dict__)
print(s1.__dict__)  # {'name': 'Mohan', 'age': 18, 'boolean': True}
print(json_txt)     # {"name": "Mohan", "age": 18, "boolean": true}

# we can see the difference between pyhon dictionary and json file

# ------------------ JSON Schema Validation ------------------
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Our blueprint for the data to add in json
# TYPE:-
# object → for dictionaries ({...})
# array → for lists ([...])
# string → for text values
# integer / number → for numeric values
# boolean → for true/false
# null → for null

user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number", "minimum": 0},
        "skills": {"type": "array", "items": {"type": "string"}},
        "is_student": {"type": "boolean"}
    },
    "required": ["name", "age"]  # These fields must be present, if any of those fields are missing, validation will fail.
}

user_data = {
    "name": "Dharmil",
    "age": 18,
    "skills": ["Python", "SQL"],
    "is_student": True
}

invalid_data = {
    "age": 15,
    "skills": ["Python"]
}

invalid_data1 = {
    "name": 12,
    "age": -5,
    "skills": ["Python"]
}

invalid_data2 = {
    "name": "dharmil",
    "age": -5,
    "skills": ["Python"]
}

# instance to what we have to check , schema is which thing we have to check
try:
    validate(instance=invalid_data2, schema=user_schema)
    print("✅ JSON is valid!")
except ValidationError as e:
    print(f"❌ Invalid JSON: {e.message}")

# ------------------ Merge 2 JSON files ------------------
def merge_json(file1, file2, output):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    merged = data1 + data2  # assumes both are lists

    with open(output, 'w') as f:
        json.dump(merged, f, indent=4, ensure_ascii=False)

merge_json('First.json', 'User.json', 'merged_users.json')

# ------------------ Handling large JSON files ------------------
import ijson

with open('User.json', 'r') as f:
    parser = ijson.items(f, 'item')
    for obj in parser:
        print(obj)   # Process one object at a time

# ------------------ Faster JSON serialization ------------------
# json is build-in python library
# use orjson which is third party library and it is 10x more fast than json
"""
| Use Case                                                                 | Best Choice               |
| ------------------------------------------------------------------------ | ------------------------- |
| Small/medium files (configs, small APIs, etc.)                           | `json` (built-in is fine) |
| Large JSON data (MBs–GBs), frequent reads/writes, APIs with high traffic | `orjson`                  |

about 80–90% of the methods are conceptually the same between json and orjson
"""

# ------------------ SUMMARY ------------------
"""
- JSON is a lightweight, structured data format for storing and exchanging data.
- Use json.dump()/json.dumps() to write, json.load()/json.loads() to read.
- ensure_ascii=False preserves Unicode characters like emojis and non-Latin text.
- Always handle exceptions: JSONDecodeError, FileNotFoundError, PermissionError, TypeError, UnicodeEncodeError.
- Use jsonschema.validate() for validating JSON structure against a schema.
- For large JSON files, consider ijson (incremental parsing) or orjson (faster serialization).
- Nested JSON can be accessed safely using custom functions like get_nested().
- Custom class objects must be converted to dicts before JSON serialization.
- Merging and appending JSON data can be automated via scripts.
- json and orjson are largely compatible, but orjson is faster for big datasets.
"""