#不定长参数

def fun(*args):   #*args基于位置传递，属于元组
    return args

print(fun(1,2,3,4,5,6))


def function(*args,**kwargs):   #  kwargs = keywords args  基于关键字传递，属于字典
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round") is not None:
        avg_data = round(avg_data,kwargs.get("round"))

    if kwargs.get("print"):
        print(f"最小值：{min_data}  最大值：{max_data}  平均值：{avg_data} （保留{kwargs.get("round")}位小数）")

function(1,4.1,6,8,9,round = 2 , print = True)