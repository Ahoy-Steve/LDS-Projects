#Exercise 3
import math
def delta(a :int , b : int, c : int):
    d=b*b-4*a*c
    if(d>0):
        print((-b+math.sqrt(d))/(2*a),(-b-math.sqrt(d))/(2*a))
    elif(d==0):
        print((-b+math.sqrt(d))/(2*a))
    else:
        print("No real solutions")
delta(2,5,3)