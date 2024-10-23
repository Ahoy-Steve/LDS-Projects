#Exercise 6
def primenumber(n, d=2):
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    elif d * d <= n:
        if n % d == 0 :
            return False
        else:
            return primenumber(n, d+1)
    else:
        return True
print(primenumber(7))

