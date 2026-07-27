#列表定义，修改，删除
list = [1,2,3,"电脑",5,6,4,True]
print(list[0])
print(list[-1])
list[-1] = 2
print(list[-1])
for i in list:
    print(i)
del list[-1]
print("_____")
for i in list:
    print(i)
print(type(list))

#列表截取
print("列表截取：----------------------------")
l = [1,2,3,4,5,6,7,8,9]
print(l[0:5:1])#l[起始索引,结束索引(不包含),步长]
print(l[0:-1:1])
#列表操作
print("列表操作：----------------------------")
a = [5,3,8,5,2,8,4,1]
print(a)
a.append(7)#尾部添加元素----a是一个对象，append是一个方法(对象.方法)
print(a)
a.insert(1,9)#在指定索引的前面插入元素
print(a)
a.remove(8)#移除第一个匹配到的值
print(a)
a.pop(5)#删除指定索引的位置
print(a)
a.sort()#对列表进行排序
print(a)
a.reverse()#反转列表
print(a)