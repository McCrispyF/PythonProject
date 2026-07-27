#字符串str 有序 不可修改 可迭代
a = "Hello Python"
print(a[4])
print(a[-4])

#可迭代:
for i in a:
    print(i)

print("--------------")
#切片[开始索引，结束索引，步长]
print(a[1:5:1])
print(a[:])
print(a[6:])

#find方法-查找
b = input("请输入想要在字符串中查找的内容")
position = a.find(b)
if position != -1:
    print(f"找到了,在第{position}位")
else:
    print("没找到")

#count方法-统计字符在字符串中出现的次数
c = "asdfghjkaadfagahhaaa"
mount = c.count("a")
print(mount)

#大小写转换
d = c.upper()
print(d)
e = d.lower()
print(e)

#split方法切割字符串 str -> list
demo = "Hello-Python-World"
demoSolit = demo.split("-")
print(demoSolit)
print(type(demoSolit))

#strip方法 去除字符串两端空格  (lstrip & rstrip 分别去除左右两边空格)
space = "   aaa   "
comp = "aaa"
print(space)
spaceDEL = space.strip()
print(spaceDEL)
if spaceDEL == comp:
    print("去除空格")
else:
    print("去除失败")

#replace方法 替换字符串中的子串
rep = demo.replace("-", " ")
print(demo)
print(rep)

#startswith endswith 方法 判断是否以指定子串开头/结尾,返回布尔值
start = demo.startswith("Hello")
end = demo.endswith("World")
print(start)
print(end)
start = demo.startswith("World")
end = demo.endswith("Hello")
print(start)
print(end)