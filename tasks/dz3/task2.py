# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.

import random
m = int(input("Введите длину списка"))
myList = []
newList = []
for i in range(m):
    myList.append(random.randint(0,50))
print(myList)

n= len(myList)
for i in range(int(n/2)):
    newList.append(myList[i]* myList[n-1-i])
if n%2 ==0:
    print(newList)
else:
    newList.append(myList[int(n/2)]**2)
    print(newList)