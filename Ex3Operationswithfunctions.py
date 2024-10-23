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