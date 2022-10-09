# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.
n = int(input("Введите число: "))
newList = [1,0,1]
for i in range(2,n+1):
    newList.append(newList[i-1]+newList[i])
for i in range(0,-n+1,-1):
    newList.insert(0,newList[1]-newList[0])
print(newList)

