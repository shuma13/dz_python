# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# НЕОБЯЗАТЕЛЬНО Попробовать решить не переводя числа в строку
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = float(input("Введите число: "))
def function_sum(n):
    res=0
    while n > 0:
        c= n%10
        res= res+c
        n=int(n/10)
    return int(res)

if number == int(number):
    result = function_sum(number)
    print(result)
else:
    c=1
    while c!=0:
        number=number*10000
        c =round(number%10)    
    number = int(number)
    res = function_sum(number)
    print(res)

