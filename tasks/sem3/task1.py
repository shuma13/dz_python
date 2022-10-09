n = input('Введите число: ')
flag = True
myList = ['vvcjukjl223', '156dvsdfgh','hjh568','155vgf']
for i in myList:
    for j in i:
        if j == n:
            print("число есть в элементе списка " +i)
            flag = False
            break
if flag:
    print('заданное число не найдено')
