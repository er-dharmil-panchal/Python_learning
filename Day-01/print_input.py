import time
# ======================================================================================================
# ======================================================================================================
# PRINT AND COMMENT
# ======================================================================================================
# ======================================================================================================

print("Hello,My name is Dharmil")
print("I am Learning Python")
     # YOU CAN ADD MULTY-LINE COMMENT USING ''' ;
'''
This is a  Comment.
'''
     # OR USE """" ;
"""
This is also too.
"""

# ======================================================================================================
# ======================================================================================================
# SEPRATER
# ======================================================================================================
# ======================================================================================================

print("heyyy",5,6,7,8,sep="--",end="123")     #SEPOutput--->  heyyy--5--6--7--8     #ENDOutput--->heyyy--5--6--7--8123heyyy**5**6**7**8321
print("heyyy",5,6,7,8,sep="**",end="321")     #SEPOutput--->  heyyy**5**6**78

# ======================================================================================================
# ======================================================================================================
# CALCULATOR
# ======================================================================================================
# ======================================================================================================

a=50
b=9
#PADMAS
print("\n",4*2-12/4)          # 5.0
print("The Value of",a," + ",b,"is",a+b)
print("The Value of",a," - ",b,"is",a-b)
print("The Value of",a," * ",b,"is",a*b)
print("The Value of",a," / ",b,"is",a/b)
print("The Value of",a," % ",b,"is",a%b)
print("The Value of",a," ** ",b,"is",a**b)
print("The Value of",a," // ",b,"is",a//b)
print("ABS OF -2.5 is",abs(-2.5))
print("Round of 2.5 is ",round(2.5))
print("Round of 2.56 is ",round(2.56))
print("2^3 using pow function ",pow(2,3))
print("div and mod for 10 and 3 is ",divmod(10,3))

# ======================================================================================================
# ======================================================================================================

     # STRING CAN'T ADD NUMBER(1,2,3,4....) , STRING CAN JOIN NUMBERS ;
a="1"
b="2"

a1=1
a2=2

print(a+b)       #  ANS 12
print(a1+a2)     #  ANS 3

# ======================================================================================================
# ======================================================================================================


# ======================================================================================================
# ======================================================================================================
# TYPECASTING
# ======================================================================================================
# ======================================================================================================

# 👉 EXPLICIT TYPECASTING (Manual Conversion)

d="ABCD"
a="1"
b="2"
e=8

print(int(a)+int(b))            # String -----> integer

c="Dharmil"

# ❌ This will cause an error: string can't convert to int
# print(int(c))

print(d,e)          # ABCD 8
print(d+str(e))     # ABCD8
print("Type cast 8 to float",float(8))
print("type cast 0 to boolean",bool(0))
print("type cast 1 to boolean",bool(1))
print("type cast \"abc\" to boolean",bool("abc"))
print("type cast \"\" to boolean",bool(""))
print("type cast \" \" to boolean",bool(" "))
print("type cast \"1 23\" to list",list("1 23"))
print("type cast \"1 23\" to tuple",tuple("1 23"))

#IMPLICIT TYPECASTING          **AUTO**


a=1.9    #Float
b=9      #Int

print(a+b)    #Float



#==========================================================================================================
#==========================================================================================================
#USER INPUT
#==========================================================================================================
#==========================================================================================================

a=input()
print(a)

b1=input("Enter Your Name : ")         #Enter Your Name  : INPUT
print("My Name is ",a)

#NOTE because it is a string

a=input("Enter First Number :")             #a=5
b1=input("Enter Second Number :")            #b=5
print(a+b1)                              #ANS = 55
print(int(a)+int(b1))                    #ANS = 10

a, c = input("Enter two numbers: ").split()
print("using .split() function ",int(a) , int(c))
print("Type of variable a",type(a))


# 🧠 Summary:
# - input() takes string input by default
# - Always typecast to int/float when needed


#==========================================================================================================
#==========================================================================================================
#EXTRA
#==========================================================================================================
#==========================================================================================================


print("hi" * 3)
print(f"my name is {c} my age is {b+10}")
print("Line1\nLine2\t\"Tabbed\"")

name = "Dharmil"
age = 20

# Using .format()
print("My name is {} and I am {} years old.".format(name, age))

# You can also use index positions
print("My name is {0} and I am {1} years old. {0} likes Python.".format(name, age))

# You can also use named placeholders
print("My name is {n} and I am {a} years old.".format(n=name, a=age))

# Formatting numbers
pi = 3.14159265
print("Value of pi up to 2 decimal places: {:.2f}".format(pi))
print(f"{pi:.2f}")  # Output: 3.14


# Right align (width = 10)
print("{:>10}".format("Hi"))

# Left align (width = 10)
print("{:<10}".format("Hi"))

# Center align (width = 10)
print("{:^10}".format("Hi"))

# Right align with padding character
print("{:_>10}".format("Hi"))

# Numeric formatting with alignment
print("{:>10.2f}".format(3.14159))




# 👉 flush concept in printing
"""
| Aspect                  | flush=False (default).                                             | flush=True.                                                          |
| ----------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------- |
| When output appears.    | Waits for buffer to fill or a newline (`\n`) before showing.       | Immediately writes output to screen after `print()` is called.       |
| Typical delay           | May appear only after several prints or at the end of the program. | No delay — updates visible instantly.                                |
| Use case                | Normal printing where timing isn't important.                      | Real-time progress updates, live logs, animations, AI training bars. |
| Example output          | In a loop, nothing may appear until it ends.                       | Output updates every loop step.                                      |
"""

print("flush=False demo:")
for i in range(5):
    print(f"\rStep {i+1}/5", end="", flush=False)  # May not appeare immediately
    time.sleep(1)

print("\n\nflush=True demo:")
for i in range(5):
    print(f"\rStep {i+1}/5", end="", flush=True)  # Appears instantly
    time.sleep(1)

print("\nDone!")

# flush=True force to appeare immidiatly after 1 loop cycle, can't wait to fill new line
print("\nDone!")  # Final newline
