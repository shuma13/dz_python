# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3






from tkinter import X
from turtle import xcor


X = float(input('Введите значение координаты x: '))
y = float(input('Введите значение координаты y: '))
if X > 0 and y > 0 :
        print('Точка находится в I четверти плоскости')
elif  X < 0 and y >0 :
        print('Точка находится в II четверти плоскости')
elif  X  < 0 and y < 0 :
        print('Точка находится в III четверти плоскости')
elif  X > 0 and y < 0 :
        print('Точка находится в IV четверти плоскости')
elif  X == 0 and y!=0  :
        print('Точка находится на оси Y')
elif y ==0 and X!=0 :
            print('Точка находится на оси X')
else:
        print ('Введены не корректные заначения координат')
