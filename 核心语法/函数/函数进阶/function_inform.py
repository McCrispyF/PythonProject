

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def calc(x,y,function):  #function代表一个函数，把函数add传进来，就执行函数add,传其他函数就执行其他函数，本质就是一个占位符
    return(function(x,y))

print(calc(1,3,add))
print(calc(1,3,sub))
print(calc(1,3,mul))
print(calc(1,3,div))
