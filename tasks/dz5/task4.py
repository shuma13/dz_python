# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbcccccccccd => 7a6b9c1d или 11a3b7c1d => aaaaaaaaaaabbbcccccccd

from itertools import count


part = 'file.txt'
with open(part, 'r', encoding ='UTF-8') as data:
   file = data.readline()

newFile = ''
count=1
for i in range(len(file)-1):
    for j in range(1,len(file)): 
        if file[i] == file[j]:
            count+=1
            if i == (len(file)-1):
                newFile =newFile + str(count) + file[j]
        else:
            newFile =newFile + str(count) + file[i]
            count=1
            if i == (len(file)-1):
                newFile =newFile + str(count) + file[j]
print(file)
print(newFile)




