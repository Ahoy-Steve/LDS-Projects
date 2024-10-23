#Exercise 4

#a
def prod_digits(n):
    if n == 0:
        return  1
    else:
        return (n % 10)*prod_digits(n // 10)
print(prod_digits(542))

#b
def count_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_digits(n // 10)
print(count_digits(3435555))

#c
def max_digit(n):
    if n < 10:
        return n
    elif n % 10 > max_digit(n // 10):
        return n % 10
    else:
        return max_digit(n // 10)
print(max_digit(543))

#d
def count_even_digits(n):
    if n < 10:
        if n % 2 == 0:
            return 1
        else:
            return 0
    else:
        if n % 2 == 0:
            return 1 + count_even_digits(n // 10)
        else:
            return  count_even_digits(n // 10)
print(count_even_digits(235))

#Exercise 7
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(16,24))

#Exercise 10

#a

def is_digit(n, x):
    if n == 0:
        return False
    elif n % 10 == x:
        return True
    else:
        is_digit(n // 10, x)
print(is_digit(204, 4))

#b
def occurrences_digit(n, x):
    if n == 0:
        return 0
    elif n % 10 == x:
        return 1+occurrences_digit(n // 10, x)
    else:
        return occurrences_digit(n // 10, x)
print(occurrences_digit(200,2))

#Exercise 12

def f(x):
    return x+1
def comp_f(f, x, n):
    if n == 0:
        return f(x)
    else:
        return f(comp_f(f, x, n-1))
print(comp_f(f,2,4))