
first=0
second=0 
result = 0

listOperator ={'*': lambda x,y: int(x)*int(y),
                '/': lambda x,y: int(x)/int(y) if y else print('деление на ноль'),
                '+': lambda x,y: int(x)+int(y),
                 '-': lambda x,y: int(x)-int(y)}

def set_first(number:int):
    global first
    first = number
def set_second(number:int):
    global second
    second = number

def Get_first():
    global first
    return first

def Get_second():
    global second
    return second

def set_result(operator: str):
    global result
    result = listOperator[operator](first,second)

def get_result():
    global result
    return result


