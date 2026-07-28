#定义类
class CarInfo:   #类名大驼峰
    pass

c1 = CarInfo()

#动态为对象添加属性 (不推荐，会降低开发可读性)
#对象名.属性名 = 属性
c1.brand = "BMW"
c1.name = "X7"
c1.price = 79

print(c1.__dict__)  #将对象中的所有属性以字典的形式输出出来
print(CarInfo.__dict__)  #将类中的所有属性以字典的形式输出出来
print(c1)