# NOTE - we can give default value in defination like this
#       def ____ ( a, b=4)
# now if we call this , ____(5), then b will be 4 as default

# Write a function fibonacci(n) that returns a list of first n Fibonacci numbers.

def fibo(n):
    a = 0
    b = 1
    c = 0
    print(a, end=',')
    for i in range(2, n+1):
        print(b, end=',')
        c = a
        a = b
        b = a+c
    print()


fibo(50)

# Write a function is_prime(num) that returns True if a number is prime, else False.


def isPrime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


print(isPrime(11))

#  Check Palindrome Number


def isPalindrome(n):
    temp = n
    rev = 0
    while temp != 0:
        rev = rev * 10 + (temp % 10)
        temp = temp//10
    return rev == n


print(isPalindrome(121))


# Vowel in String

def vowel(text):
    txt = text.lower()
    count = 0
    for i in txt:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            # if (i in 'aeiou'):
            count += 1
    return count


print(vowel("DhArmil"))

# Check if Number is Armstrong Number


def arm(n):
    length = len(str(n))
    temp = n
    sum = 0
    while temp!=0:
        sum += pow((temp%10),length)
        temp //= 10
    return sum == n
print(arm(153))
