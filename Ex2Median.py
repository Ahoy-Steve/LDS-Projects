#Exercise 2
def median(a,b,c):
    s=a+b+c
    return s-max(a,b,c)-min(a,b,c)
print(median(1,2,3))