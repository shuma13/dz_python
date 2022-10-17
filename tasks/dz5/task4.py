# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#  Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbcccccccccd => 7a6b9c1d или 11a3b7c1d => aaaaaaaaaaabbbcccccccd

from itertools import count


part = 'file.txt'
newPart = 'newFile.txt'
secondPart = 'text.txt'
newSecond = 'newtext.txt'
with open(part, 'r', encoding ='UTF-8') as data:
   file = data.readline()

newFile = ''
count=1
for i in range(1,len(file)): 
    if file[i] == file[i-1]:
        count+=1
    else:
        newFile =newFile + str(count) + file[i-1]
        count=1
        if i == (len(file)-1):
            newFile =newFile + str(count) + file[i]        
print(file)
print(newFile)
with open(newPart, 'w', encoding ='UTF-8') as data:
   data.write(newFile)
with open(secondPart, 'r', encoding ='UTF-8') as data:
   sfile = data.readline()
print(sfile)
num =''
strnum =''
for i in sfile:
    if i.isdigit():
        num = num +i
    else:
        number = int(num)
        strnum += i * number
        num = '' 
print(strnum)
with open(newSecond, 'w', encoding ='UTF-8') as data:
   data.write(strnum)





