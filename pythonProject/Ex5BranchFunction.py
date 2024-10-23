#Exercise 5
def f(x:int):
    if(x<-3):
        return 2*x+1
    elif(x==-3):
        return 0
    else:
        return 3*x*x+6*x-5
print(f(-4))
print(f(-3))
print(f(-2))

