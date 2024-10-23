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