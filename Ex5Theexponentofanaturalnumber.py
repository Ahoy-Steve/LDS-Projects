#Exercise 5
def exponetial(a, n):
    if n == 0:
        return 1
    else:
        return a*exponetial(a, n-1)
print(exponetial(2,5))