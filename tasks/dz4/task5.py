# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0
# Код на основе семинара!
part = 'file.txt'
partWrite = 'newFile.txt'
partSum = 'sumEquation.txt'
with open(part, 'r', encoding ='UTF-8') as data:
   equation1 = data.readline()
with open(partWrite, 'r', encoding ='UTF-8') as data:
   equation2 = data.readline()
print(equation1)
print(equation2)
def parseEquattion (equation: str):
    eqDict = {}
    equation = equation.replace('+', ' '). replace('-',' -'). replace('=0','')
    equation = equation.split()
    for i in equation:
        element = i.split('*x^')
        eqDict[int(element[1])] = int(element[0])
    return eqDict
eqDict1 = parseEquattion (equation1)
eqDict2 = parseEquattion (equation2)
print(eqDict1)
print(eqDict2)
def SumEquation (dict1, dict2):
    SumDict ={}
    for i in range(max(len(eqDict1),len(eqDict2)),-1,-1):
        if eqDict1.get(i) or eqDict2.get(i):
            SumDict[i] = (eqDict1.get(i) if eqDict1.get(i) else 0) +(eqDict2.get(i) if eqDict2.get(i) else 0)
    return SumDict
FinalDict = SumEquation (eqDict1, eqDict2) 
print(FinalDict)
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

sumEqation = f'{creatEqation(FinalDict)} =0'
print(sumEqation)
with open(partSum, 'w', encoding ='UTF-8') as data:
   data.write(sumEqation)    