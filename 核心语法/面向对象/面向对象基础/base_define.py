class Car:
    # __init__方法 对象创建时自动执行 用于初始化
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car初始化完毕")

    def running(self):
        print(f"{self.brand}{self.name}高速行驶中...")

    def total_cost(self,discount,rate):
        total = self.price * discount + self.price * rate
        return total
c1 = Car("红色","BMW","X5",500000)#创建c1后，各个方法里的self 都是指 c1
total1 = c1.total_cost(0.85,0.05)
print(total1)