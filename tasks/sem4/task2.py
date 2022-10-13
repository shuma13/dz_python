part = 'text.txt'

with open(part, 'r', encoding ='UTF-8') as data:
   data_file = data.readline()

   print(data_file)