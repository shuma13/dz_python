# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов. 
#  Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении
#   не участвует

myList = [1.1, 1.2, 3.1, 5, 10.01]
newList =[]
for i in myList:
    newElm = int(i)
    c= round(i%newElm,2)
    if c != 0:
        newList.append(c)
print(newList)
max = newList[0]
min = newList[0]
for i in newList:
    if i > max:
        max = i
    elif i< min:
        min = i
print(max)
print(min)
print(max-min)


