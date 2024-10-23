
def leapyear(y :int):
    if(y%400==0):
        return  True
    elif(y%100==0):
        return False
    elif(y%4==0):
        return True
    else:
        return False

def nrdays(y1:int , y2:int):
        y=abs(y2-y1)
        days=365*y
        days=days+int(y/4)
        if leapyear(y1)==True & leapyear(y2)==True:
                days=days+1
        return days
print(nrdays(2000,2024))