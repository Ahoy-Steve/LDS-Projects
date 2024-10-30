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
list1=[1,2,3,4,5,6,7]
list2=list(filter(primenumber,list1))
print(list2)



def primenumber(n, d=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return primenumber(n, d + 1)

# list1 = [1, 2, 3, 4, 5, 6, 7, -1, -5]

tastatura = input("Introduceti numerele pentru lista (separate prin spațiu): ")
list1 = list(map(int, tastatura.split()))
list2 = list(filter(primenumber, list1))
print(f"Lista cu numere prime: {list2}" )

