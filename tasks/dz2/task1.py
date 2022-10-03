number = float(input("Введите число: "))
def function_sum(n):
    res=0
    while n > 0:
        c= n%10
        res= res+c
        n=int(n/10)
    return res

while number != int(number):
    number=number*10
    print(number) 
result = function_sum(number)
print(result)
