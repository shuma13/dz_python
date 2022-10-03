# string = "hsgfcwenwentfasfdasdfsagfgjfwenjkwwqfdgwenvdsfwent"
# substring = "wen"
# count = 0
# buffer = 0
# lengthSubstring = len(substring)
# lengthString = len(string)
# for i in range(lengthString - lengthSubstring+1):
#     for j in range(lengthSubstring):
#         if string[i+j] != substring[j]:
#             buffer = 0
#             break
#         elif string[i+j] == substring[j]:
#             buffer += 1
#             if buffer == lengthSubstring:
#                 count += 1
#                 buffer = 0
#                 continue
# print(count)

string = input('Введите строку: ')
substring = input('Введите строку для поиска: ')
n = 0

if string.find(substring) == -1:
    print("Совпадений нет")
else:
    n = 1
    new_string = string[(string.find(substring) + len(substring)):]
    while new_string.find(substring) != -1:
        n += 1
        new_string = new_string[(new_string.find(substring) + len(substring)):]

print(n)


