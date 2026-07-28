#定义类
class CarInfo:
    # __init__方法 对象创建时自动执行 用于初始化
    def __init__(self,c_brand,c_name,c_price):
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.print("CarInfo初始化完毕")

c1 = CarInfo("BMW","X5",500000)

print(c1)