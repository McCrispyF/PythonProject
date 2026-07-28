"""
def 函数名(参数)
    函数体
    return 返回值
"""

#函数定义
def out_line():
    print("----------------")

#函数调用
out_line()

def circle_area(radius):
    """
    函数可以计算圆的面积和周长
    :param radius: 圆的半径
    :return: 圆的面积，圆的周长
    """
    return round(3.14 * radius * radius,2),round(2 * 3.14 * radius,2)

r = float(input("请输入圆的半径："))
area,length = circle_area(r)
print(f"面积 = {area},周长 = {length}")