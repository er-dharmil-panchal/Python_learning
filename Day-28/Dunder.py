# Before dunder methods , we will learn dir,__dict__,help
import json

# ========================
# dir
# ========================
# The dir function returns a list of all the attributes and methods
# (including dunder methods) available for an object.

a = [1, 12, 13, 26]
print(dir(a))


# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
# '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
# '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index',
# 'insert', 'pop', 'remove', 'reverse', 'sort']


# ========================
# __dict__
# ========================
# __dict__ attribute (already learn previously)
# The __dict__ attribute returns a dictionary
# representation of an object's attributes. It is a useful tool for introspection.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Maan", 20)
print(s1.__dict__)  # {'name': 'Maan', 'age': 20}

# ========================
# help
# ========================
# help :- : The help function is used to get help documentation for an object,
# including a description of its attributes and methods.
# can use for any object, str,list, tuple, custom object etc...

print(help(Student))
"""
class Student(builtins.object)
 |  Student(name, age)
 |
 |  Methods defined here:
 |
 |  __init__(self, name, age)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object

"""

# ========================
# Magic/Dunder methods
# ========================
"""
 📌 Magic/Dunder methods :-  Dunder = Double Underscore ( __ )
        -Python calls them automatically in certain situations.

    some Example:- 
        - When you use +, Python internally calls __add__.
        - When you use len(), Python internally calls __len__.
        - When you print an object, Python calls __str__.
"""


class Dog:
    a = [1, 2, 3]

    def __init__(self, name, filename="dog.txt"):
        self.name = name
        self.filename = filename

    def __str__(self):
        return f"Dog’s name is {self.name}"

    def __repr__(self):
        return f"Dog(name='{self.name}')"

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        return self.a[index]

    def __setitem__(self, index, value):
        self.a[index] = value

    def __delitem__(self, index):
        del self.a[index]

    def __iter__(self):
        return self

    limit = 4
    start = 0

    def __next__(self):
        if self.start < self.limit:
            self.start += 1
            return self.start
        else:
            raise StopIteration

    def __call__(self, name):
        return f"Hello, {name}!"

    def __contains__(self, a):
        return a in self.a

    def __del__(self):
        print("Object destroyed")

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")
        self.file.close()


# 1. __init__ :- already used in class as a constructor
# __init__ runs automatically when we create an object.
dog1 = Dog("Tommy")

# 2. __str__ :-
# Without __str__, print(dog1) would show something ugly like <__main__.Dog object at 0x000...>
print(dog1)  # Dog’s name is Tommy

# 3. __repr__ → Official String Representation (for developers)
print(repr(dog1))

# 4. __len__ → Length of Object
print(len(dog1))

# 5. __getitem__ → Indexing / Slicing
print(dog1[0])

# 6. __setitem__ → Assigning with Index
dog1[2] = 4
print(dog1[2])

# 7. __delitem__ → Deleting with Index
del dog1[2]
# print(dog1[2])

# 8. __iter__ & __next__ → Iteration
for num in dog1:
    print(num)  #

# 9. __eq__, __lt__, __gt__ → Comparisons (Already learned)

# 10. __add__ (and other math ops like __sub__, __mul__, etc.) (Already learned)

# 11. __call__ → Make Object Callable
print(dog1("Tomy"))

# 12. __contains__ → in keyword
print(1 in dog1)
print(4 in dog1)

# 13. __del__ → Destructor
del dog1

# 14. __enter__ and __exit__
# Used in context managers (with-statement).
with Dog("Tommy", "dog.txt") as f:
    f.write("Hello World")

# the Dog object also gets destroyed after the with block ends.
