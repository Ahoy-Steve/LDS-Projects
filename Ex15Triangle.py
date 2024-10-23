#Exercise 15
def triangle(n):
    if n == 0:
        return 0
    else:
        triangle(n-1)
        print(str(n)*n)
triangle(5)