api = input("请输入名字:")
print(api)
print(type(api))

a = """
    hello world
    你好
    我是python三引号字符串
    """
print(a)
b = "hello python"
print(f"我是:{a}&{b}")

#运算
a = 10
b = 3
c = a + b
print("a + b = " + str(c))
c = a - b
print("a - b = " + str(c))
c = a * b
print("a * b = " + str(c))
c = a / b
print("a / b = " + str(c))
c = a // b
print("a // b = " + str(c))#整除
c = a % b
print("a % b = " + str(c))#取余数
c = a ** b
print("a ** b = " + str(c))#次方运算

#条件判断
num = int(input("请输入年龄:"))
if(num < 18):
    print("未成年人")
elif(num >= 18 and num <= 50):
    print("成年人和中年人")
else:
    print("老年人")

