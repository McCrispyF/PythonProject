#全局变量
num = 100
ber = 100

def register(name,age,high,city = "北京"):  #指定了北京为默认参数（缺省参数），缺省参数必须放到未设置默认值的参数之后
    print(name,age,high,city)
    num = 10000 #定义局部变量
    print(num)
    global ber #调用全局变量
    ber = 200
    print(ber)

register("王林","20",high = "171")
print(num)
