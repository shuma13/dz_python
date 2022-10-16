# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
myList = ['Вороне', 'какабвто', 'Богабв', 'послал', 'кусоабвчек', 'сыра']
substring = input('Введите строку для поиска: ')
n = len(substring)
newList = []
buffer =0
flag = True
for i in myList:
    buffer =0
    flag = True
    lenStr = len(i)
    for j in range(lenStr - n+1):
        for y in range(n):
            if i[j+y] != substring[y]:
                break
            elif i[j+y] == substring[y]:
                buffer+=1
                if buffer == n:
                    flag = False
    if flag:
        newList.append(i)
print (newList)


