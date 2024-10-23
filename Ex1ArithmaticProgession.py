#Exercise 1
def arith_progession(n):
    if n==0:
        return 2
    else:
        return 2*arith_progession(n-1)-3
print(arith_progession(1))