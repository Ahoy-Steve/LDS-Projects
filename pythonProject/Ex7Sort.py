def Sort(a,b,c):
    s=a+b+c
    return (max(a,b,c), s-max(a,b,c)-min(a,b,c), min(a,b,c))
print(Sort(1,2,3))