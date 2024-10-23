#Exercise 1

#v1
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
#V2

def numar_valori_distincte(arg1, arg2, arg3):
    distinct = len(set([arg1, arg2, arg3]))

    if distinct == 3:
        print("Toate argumentele sunt distincte")
    elif distinct == 2:
        if arg1 == arg2:
            print(f"Arguments {arg1} and {arg2} are equal")
        elif arg2 == arg3:
            print(f"Arguments {arg2} and {arg3} are equal")
        elif arg1 == arg3:
            print(f"Arguments {arg1} and {arg3} are equal")
    elif distinct == 1:
        print("Toate argumentele sunt egale")

