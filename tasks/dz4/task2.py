# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

string = input('Введите последовательность цифр:  ')
myList =[]
flag =True
for i in range(0, len(string)):
    flag = True
    
    for j in range(0,len(string)):
        
        if j!= i:
            if string[i] == string[j]:
                flag =False
                break
    if flag:
        myList.append(string[i])
print(myList)
