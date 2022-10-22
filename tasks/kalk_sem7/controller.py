
import view, model

def start():
    a= view.InputData('A')
    model.set_first(a)
    while True:

        oper = view.InputOperator()
        if oper == "=": break
        b= view.InputData('B')
        model.set_second(b)
        model.set_result(oper)
        result = model.get_result()
        if result == None: break
        view.outputResult(result)
        model.set_first(result)
    view.outputResult(result)    

def PrintValues():
    a = model.Get_first
    b = model.Get_second
    view.outputData(a)
    view.outputData(b)
    
def PrintResult():
    result = model.splitData()
    view.outputResult(result)

# def solution():
#     oper = view.InputOperator()
#     model.set_result(oper)
#     result = model.get_result()
    # view.outputResult(result)