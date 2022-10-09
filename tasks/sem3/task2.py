myList = ['vvcjukjl223', '156dvsdfgh','hjh568','155vgf']
n= input('Введите искомую строку: ')
flag = True
count =0
for element in myList:
    for i in range(len(element)):
        if element[i:i+len(n)] == n:
            count+=1
            if count ==2:
                print(element)
                flag = False
                break
if flag:
    print("Второго вхождения нет")
    
myList = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
num=input("Введите искомую строку: ")
buffer = 0
count = 0
for element in range(0,len(myList)-1):
if num==myList[element]:
count+=1
if count == 2:
buffer = element
if count == 2:
print(buffer)
else:
print("-1")
