def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multyply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        raise ValueError("can not devide by zero!")
    return x/y