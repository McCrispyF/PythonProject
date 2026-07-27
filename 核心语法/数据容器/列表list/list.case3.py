#生成1-20的平方列表

num_list1 = []
for i in range(1,21):
    num_list1.append(i ** 2)
print (num_list1)

num_list2 = [i ** 2 for i in range(1,21)]
print (num_list2)

#从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表
#经典写法
"""
num_list = [12,44,13,75,24,61,6,53,22]
new_list = []
for i in num_list:
    if i % 2 == 0:
        new_list.append(i ** 2)
print(new_list)
"""

#列表推导式
num_list = [12,44,13,75,24,61,6,53,22]
new_list = [i ** 2 for i in num_list if i % 2 == 0]
print(new_list)