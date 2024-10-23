#Exercise 13

#a
def S1(n):
    if n == 1:
        return 1;
    else:
        return 1/n+S1(n-1)
print(S1(4))

#b
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
def power(x, n):
    if n == 0:
        return 1;
    else:
        return x*power(x, n-1)
def taylor(x, n):
    if n == 0:
        return 1
    else:
        return power(x,n)/factorial(n)+taylor(x, n-1)
print(taylor(2, 3))

#c
import math
def S3(n):
    if n == 0:
        return 1
    else:
        return round(math.sqrt(1+ S3(n-1)),10)
print(S3(3))