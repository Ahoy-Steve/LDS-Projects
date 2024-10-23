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