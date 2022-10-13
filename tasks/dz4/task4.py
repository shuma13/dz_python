# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 
# до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем
#  данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
# КОД ПРАВИЛА СВОЙ НА ОСНОВЕ СЕМИНАРА, ВСЕ РАБОТАЕТ.
import random
import string
stMng = " "
k = int(random.randint(3,10))
equation ={}
part = r'file.txt'
for i in range(k,-1,-1):
    equation[i] = random.randint(-100,100)
def creatEqation(equation: dict):
    stMng =''
    first = True
    for k,v in equation. items():
        if first:
            first = False
        if v>0:
            stMng += f'+{v}*x^{k}'
        elif v<0:
            stMng +=f'-{abs(v)}*x^{k}'
    return stMng

strEqation = f'{creatEqation(equation)} =0'
print(strEqation)
with open(part, 'w', encoding ='UTF-8') as data:
   data.write(strEqation) 

print(equation)
