import random
import string
size = random.randint(5,10)
string = ""
part = r'text.txt'
partWrite = r'newtext.txt'
for _ in range(size):
    string += f'{random.randint(1,9999)} '


with open(part, 'w', encoding ='UTF-8') as data:
   data.write(string[:-1]) 

with open(part, 'r', encoding ='UTF-8') as data:
   data_file = data.readline()

file = data_file.split(' ')
for i in range(len(file)):
    file [i] = int(file[i])

result = str(min(file)) + '=>' + str(max(file))
with open(partWrite, 'w', encoding ='UTF-8') as data:
   data.write(data_file + '\n')
   data.write(result)

