# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.

import random


myList = []
sum = 0
for i in range(10):
    myList.append(random.randint(0,50))
for i in range(len(myList)):
    if i%2 != 0 :
        sum += myList[i]
print(myList)
print(sum)

