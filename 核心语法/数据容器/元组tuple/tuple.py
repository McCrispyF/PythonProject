tuple1 = ()
tuple2 = (100,)
tuple3 = (100,2,53,11,53,12,63,2,2,553,1,0)
print(tuple2)

#count方法，统计某元素在元组中出现的次数(同list.count)
count_2 = tuple3.count(2)
print(count_2)

#index方法,查找某个元素的索引位置（第一次出现）
location_1 = tuple3.index(2)
print(location_1)


#组包&解包
#定义元组即为组包
t1 = (1,2,3,4)

#基础解包
print("基础解包-------------------")
a,b,c,d = t1
print(t1)
print(a)
print(b)
print(c)
print(d)

#(*)扩展解包  (收集剩余所有元素）
print("扩展解包-------------------")
x,*y,z = t1
print(x)
print(type(x))#int
print(y)
print(type(y))#list
print(z)