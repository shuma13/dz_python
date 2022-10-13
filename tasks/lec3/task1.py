part = r'lec3.txt'
with open(part, 'r', encoding ='UTF-8') as data:
   data_file = data.readline()
   print(data_file)

   file = data_file.split(' ')
   for i in range(len(file)):
    file[i] = int(file[i])
print(file)
def f(x):
    return x**2
file = [(file[i], f(file[i])) for i in range(len(file)) if file[i]%2 ==0]
print(file)