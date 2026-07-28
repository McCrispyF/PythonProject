#dict  存储的是 键值对  key:value   可以根据 key 寻找到 value   key不能重复
dict1 = {"王林":675,"李慕婉":608,"许立国":478}
name = "王林"
score = dict1[name]
print(type(dict1))
#访问
print(f"{name}的高考分数是：{score}")

#添加
dict1["李浩然"] = 588
print(dict1)

#删除
dict1.pop("王林")
print(dict1)

del dict1["许立国"]
print(dict1)

#修改
dict1["李慕婉"] = 688
print(dict1)

#查询
print(dict1["李浩然"])
print(dict1.get("李浩然"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

#遍历
for i in dict1.keys():
    print(i, dict1[i])

for i in dict1.items():
    print(i)

for k,v in dict1.items():
    print(k, v)