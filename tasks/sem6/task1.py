data = input('Введите выражение: ')
prioritet = ["*", "/", "+", "-"]

listResult = []
listResult = data.replace("+", " + ").replace("-",
" - ").replace("*", " * ").replace("/", " / ")

listResult = listResult.split()

while len(listResult) > 1:
    if prioritet[0] in listResult or prioritet[1] in listResult:
        for i in range(1, len(listResult)-1):
            if listResult[i] == prioritet[0]:
                listResult[i-1] = int(listResult[i-1])*int(listResult[i+1])
                break

            elif listResult[i] == prioritet[1]:
                listResult[i-1] = int(listResult[i-1])/int(listResult[i+1])
                break
    else:
        for i in range(1, len(listResult)-1):

            if listResult[i] == prioritet[2]:
                listResult[i-1] = int(listResult[i-1])+int(listResult[i+1])
                break
            elif listResult[i] == prioritet[3]:
                listResult[i-1] = int(listResult[i-1])-int(listResult[i+1])
                break
    listResult.pop(i)
    listResult.pop(i)

print(f'{data} = {listResult[0]}')