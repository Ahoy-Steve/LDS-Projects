import math
#Exercise 1
def Last_Digit(x):
    return abs(x%10)
print(Last_Digit(234))

#Exercise 2
def molecular_mass(c,h,o):
    return 12*c+1*h+16*o
print(molecular_mass(2,2,2))

#Exercise 3
def delta(a :int , b : int, c : int):
    d=b*b-4*a*c
    if(d>0):
        print((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a))
    elif(d==0):
        print((-b+math.sqrt(d))/(2*a))
    else:
        print("No real solutions")
delta(2,5,3)

#Exercise 4
def leapyear(y :int):
    if(y%400==0):
        return  True
    elif(y%100==0):
        return False
    elif(y%4==0):
        return True
    else:
        return False
print((leapyear(2020)))

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

#Exercise 6
def interval(a,b,c):
    return ((a<=c) & (c<=b))
print(interval(3,5,6))

#Exercise 7
def Sort(a,b,c):
    s=a+b+c
    return (max(a,b,c),s-max(a,b,c)-min(a,b,c),min(a,b,c))
print(Sort(1,2,3))

#Exercise 8
def dep_arrvialtime(d,a):
    h1=int(d[0:2])
    h2=int(a[0:2])
    if (h2==0):h2=24
    h=abs(h2-h1)*3600
    m=abs(int(a[3:5])-int(d[3:5]))*60
    s=abs(int(a[6:8])-int(d[6:8]))
    return h+m+s

print(dep_arrvialtime("04:01:00","11:30:00"))

#Exercise 9
def circle(r):
    return [2*math.pi*r,math.pi*r*r]
print(circle(5))

#Exercise 10
def nrdays(y1: int, y2: int):
    return int(365 * (((abs(y1 - y2)) - int(abs(y1 - y2)) / 4) - 1) + 366 * (int(abs(y1 - y2)) / 4 + 1))
print(nrdays(2000, 2024))