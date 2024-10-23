#Exercise 9
def interval(a, b):
    if b == a:
        print(a)
    else:
        print(b)
        return interval(a, b - 1)

interval(4, 9)