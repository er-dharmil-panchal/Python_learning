"""
After learning basics of file io concepts like opening, closing, modes, etc...
Now we are learning new methods of file_io
"""

# -------------------------------
# Reading file content
# -------------------------------
f = open("file_io/sample.txt")
print(f.read())

# readline() & writeline()
while True:
    line = f.readline()
    print(line)
    if not line:
        print(type(line))
        break

# -------------------------------
# Working with marks.txt
# -------------------------------
# marks.txt ->
#   55,23,88
#   98,35,77
#   34,78,35

mark = open("file_io/marks.txt", '+r')
printInFile = open("file_io/sample3.txt", 'w')
# mark2 = open("file_io/marks.txt", 'a')

i = 0
while True:
    line = mark.readline()
    if not line:
        break

    marks1 = line.split(",")[0]
    marks2 = line.split(",")[1]
    marks3 = line.split(",")[2]

    try:
        sum = int(marks1) + int(marks2) + int(marks3)
    except ValueError as e:
        print(e)

    # mark.writelines(f"Total marks of student {i+1} is {sum}")
    # OR
    # mark.writelines(f"Total marks of student {i+1} is {sum}")
    # NOTE: after this file cursor reaches the end of file due to writing.

    demo = f"Total marks of student {i+1} is {sum}\n"
    print(demo)
    printInFile.write(demo)
    i += 1

# -------------------------------
# Writing iterable objects
# -------------------------------
# Iterable objects in Python (list, set, tuple, dictionary)
# can be used to write line by line content in a .txt file
file = ("Dharmil", "Panchal")
printInFile.writelines(file)

# NOTE: writelines method does not add newline characters
#       between the strings in the sequence.

printInFile.close()
f.close()
mark.close()

# -------------------------------
# Using seek(), tell(), truncate()
# -------------------------------
"""
In Python, the seek and tell functions are used to work with file objects
and their positions within a file. These functions are part of the built-in
io module, which provides a consistent interface for reading and writing to
various file-like objects, such as files, pipes, and in-memory buffers.

The tell function returns the current position within the file, in bytes.
"""

with open("file_io/sample3.txt", 'a+') as smp3:
    smp3.seek(3)            # cursor will point the 3rd character of the file
    print(smp3.tell())      # 3
    print(smp3.read(5))     # next 5 characters will be printed
    smp3.write("hiiii")
    smp3.truncate(3)
