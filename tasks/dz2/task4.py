# Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него) 
# можно (нужно) использовать библиотеку Random
import random
list = [2,85,15,4,72,6,14]
print(list)
n = len(list)
for i in range(n):
    j = random.randint(0,n-1)
    c = list.pop(j)
    list.append(c)

print(list)
