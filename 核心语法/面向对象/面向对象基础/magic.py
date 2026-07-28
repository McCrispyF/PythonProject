#魔法方法不用自己调用
#  __init__  创建对象自动调用，初始化
#  __str__   字符串表示的方法
#  __eq__    比较两个对象是否相等
#  __lt__ __le__ __gt__ __ge__   表示两个对象的大小
#lt : less than     le : less than or equal
#gt : greater than  ge : greater than or equal

#定义类
class Car:
    # __init__方法 对象创建时自动执行 用于初始化

    #类属性 所有实例对象共享  查找时先查找实例属性，再查找类属性
    wheel = 4
    def __init__(self,c_brand,c_name,c_price):
        #实例属性           查找时先查找实例属性，再查找类属性
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("CarInfo初始化完毕")

    def __str__(self):
        return f"{self.brand} {self.name} {self.price}"

    def __eq__(self,other):
        return self.brand == other.brand and self.name == other.name and self.price == other.price

    def __lt__(self,other):
        return self.price < other.price

c1 = Car("BMW","X5",500000)
c2 = Car("BMW","X5",500000)
c3 = Car("BMW","X3",300000)


print(c1)
print(c1.__str__())
print(c1.__eq__(c2))
print(c1.__lt__(c3))