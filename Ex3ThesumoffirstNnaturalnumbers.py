#Exercise 3
def sumNat(n):
    if n == 0:
        return 0
    else:
        return n+sumNat(n-1)
print(sumNat(4))
