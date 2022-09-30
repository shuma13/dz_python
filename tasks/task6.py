# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
from xmlrpc.client import boolean


x = boolean(input('Введите значение 0 или 1  для x: '))
y = boolean(input('Введите значение 0 или 1  для y:'))
z = boolean(input('Введите значение 0 или 1  для z:'))
res_1 = not (x or y or z)
res_2 = (not x) and (not y) and (not z)
print(res_1 == res_2)
