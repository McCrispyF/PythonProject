#计算阶乘

def jc(n):   #递归调用:函数自己调用自己 要有终结点
    if n == 1:
        return 1
    else:
        return(n * jc(n - 1))

result = jc(10)
print(result)