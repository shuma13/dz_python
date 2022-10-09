# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
n = int(input("Введите число: "))
newList = []
while n>0:
     c= n%2
     n= n//2
     newList.append(c)
print(newList)
n= len(newList)
for i in newList:
    print(newList[n-1], end ='')
    n-=1
