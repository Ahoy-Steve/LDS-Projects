# list1=[1,2,3,4,5]
list1= input("Choise ur number for ur list ( separated by space): ")
num = list(map(int, list1.split()))
list2=list(map(lambda x: x ** 3 ,num[:3]))
print("Lista cu primele elemente ridicate la puterea a treia:", list2)

