# ==========================================================================================================
#                                   Loop - practice
# ==========================================================================================================

#   👉🏻  Easy
n = int(input("Enter number"))
print("\nE-1.Right-angled Triangle with Increasing Numbers:")

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()

print("\nE-2.Inverted Triangle with Decreasing Numbers:")

for i in range(1, n+1):
    for j in range(1, n+2-i):
        print(j, end='')
    print()


#   👉🏻  Medium

print("\nM-1.Centered Pyramid with Stars:")

for i in range(1, n+1):
    # space
    for j in range(1,n+1-i):
        print(end=' ')
    for k in range(1,i*2):
        print("*",end='')
    print()

print("\nM-2.Floyd's Triangle (Numbers increasing across rows):")

count = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(count,end='. ')
        count = count +1
    print()

print("\nM-3.Alphabet Pyramid:")

alpha = 'A'

for i in range(1,n+1):
    #space
    for j in range(1,n+1-i):
        print(end=' ')
    for k in range(1,i*2):
        print(alpha,end='')
        alpha = chr(ord(alpha)+1)
    print()

#   👉🏻  Hard

print("\nH-1.Diamond Shape with Stars:")

for i in range(1, n+1):
    if(i<=int(n/2)+1):
    #space
        print(' '*(int(n/2)+1-i),end='')
   
        for j in range(1, i*2):
            print("*",end='')
        print()
    else:
        print(' '*(i+2-n),end='')

        for k in range(1,(n-i+1)*2):
            print("*",end='')
        print()