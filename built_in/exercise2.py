import functools

def filterReduce(list):
    response=filter(lambda x:x%2 ,list)
    response=functools.reduce(lambda x, y: x+y ,response)
    return f'Resultado del reduce=> {response}'

list=[i for i in range(1,101)]
print(filterReduce(list=list))