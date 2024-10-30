import functools

list1=[1,2,3,4,5]

print(functools.reduce(lambda a,b:a*b,list1))


from functools import reduce

# Funcția care va înmulți două numere
def multiply(x, y):
    return x * y

# Exemplu de listă de numere reale
numbers = [1, 2 , 3 , 4 , 5]

# Folosim reduce pentru a înmulți toate elementele din listă
result = reduce(multiply, numbers)

# Afișăm rezultatul
print("Produsul tuturor elementelor din listă:", result)
