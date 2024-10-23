#Exercise 1
def f(a:int ,b:int)->int:
    if a==b:
        return 1
    else:
        return 0
def distval(a,b,c):
    ok1=f(a,b)
    ok2=f(b,c)
    ok3=f(a,c)
    if ok1==1 & ok2==1 & ok3==1 :
        print("all arguments are equal")
        return 0
    elif ok1==1 & ok2==0 & ok3==0:
        print("arguments 1 and 2 are equal")
        return 1
    elif ok1==0 & ok2==1 & ok3==0 :
        print("arguments 2 and 3 are equal")
        return 1
    elif ok1==0 & ok2==0 & ok3==1 :
        print("arguments 1 and 3 are equal")
        return 1
    elif ok1==0 & ok2==0 & ok3==0 :
        print("all arguments are distinct")
        return 3

#Exercise 2
def median(a, b, c):
    s = a + b + c
    return s - max(a, b, c) - min(a, b, c)
print(median(1, 2, 3))

#Exercise 3
import operator
def f(x):
    return x+1
def g(x):
    return x+2
def generic_op(op,x,y):
    return op(x,y)
def sum(f,g):
    return lambda x: generic_op(operator.add,f(x),g(x))
def dif(f,g):
    return lambda x: generic_op(operator.sub,f(x),g(x))
print(sum(f,g)(4))
print(dif(f,g)(4))

#Exercise 4
def f(x):
    return (lambda x:x+15)(x)
print(f(2))

#Extra exercise
def f(x):
    return x +1
print(f(1))

def f(x):
    return x+1
print(f(1))

def f(x):
    return x+1
print(f(1))

def f(x):
    if x==0:
        return True
    else:
        return False
print(f(1))

def f(x):
    if x==0:
        return True
    else:
        return False
print(f(1))

def f(x):
    if x==0:
        return True
    else:
        return False
print(f(1))

def f(x):
    if x==0:
        return True
    else:
        return False
print(f(1))

def f(x):
    return x +1
print(f(1))

def f(x):
    return x+1
print(f(1))

def f(x):
    return x+1
print(f(1))

def f(x):
    if x==0:
        return True
    else:
        return False
print(f(1))

def f(x):
    if x==0:
        return True
    else:
        return False
print(f(1))

def f(x):
    if x==0:
        return True
    else:
        return False
print(f(1))

def f(x):
    if x==0:
        return True
    else:
        return False
print(f(1))

def f(x):
    if x == 0:
        return True
    else:
        return False
print(f(1))

def f():
    print("Fast food")

def f(x):
    return x + 1

def f(x):
    return x + 1

def increment(x):
    return x +1
print(increment(5))

def increment(x):
    return x+1
print(increment(5))

def increment(x):
    return x + 1
print(increment(5))

import math
math.floor(3)

import math
math.floor(3)

def split(x , y):
    return x/y
print(split(1, 2))

def f(x):
    return x+5
print(f(1))