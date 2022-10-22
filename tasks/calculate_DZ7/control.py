import view, model

def start():
    data = view.InputData()
    model.set_math(data)
    model.set_result(data)
    result = model.get_result()
    view.outputResult(result)

