#Exercise 12
def f(x):
    return x+1
def comp_f(f, x, n):
    if n == 0:
        return f(x)
    else:
        return f(comp_f(f, x, n-1))
print(comp_f(f,2,4))