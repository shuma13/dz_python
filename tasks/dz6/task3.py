# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов. 
#  Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении
#   не участвует
# Использованны: map,lambda, zip, filter, enumerate

from cProfile import label


myList = [1.1, 1.2, 3.1, 5, 10.01]
newList =list(map(lambda x: round(x%int(x),2), myList ))
FList = list(zip(myList, newList))

# for i in myList:
#     newElm = int(i)
#     c= round(i%newElm,2)
#     if c != 0:
#         newList.append(c)
print(newList)
print(FList)
newList = list(filter(lambda x: x!=0, newList ))
print(newList)
max = newList[0]
min = newList[0]
max_ind = 0
min_ind = 0
for i,k in enumerate(newList):
    if k > max:
        max = k
        max_ind = i
    elif k< min:
        min = k
        min_ind = i
print(max)
print(min)
print(max-min)
print(max_ind)
print(min_ind)


