#Exercise 16
def power(a, k):
    if k == 0:
        return 1
    else:
        return a*power(a,k-1)
def modulo(a, p, k=0):
    if a % p == 0:
        return 0
    elif a % p == 1:
        if k == 0:
            return 1
        else:
            return k
    else:
        return modulo(power(a,k+1),p,k+1)
print(modulo(8,7))