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