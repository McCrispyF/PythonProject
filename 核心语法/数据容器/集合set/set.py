#自动去重-用于存储不可重复的数据（手机号、身份证号）
#无序、不可重复、可修改

s1 = {5,3,7,2,1,6}
s2 = set()
print(s1)

s1.add(12)
print(s1)

s1.remove(1)
print(s1)

#随机删除一个元素并返回
print(s1.pop())
print(s1)

s1.clear()
print(s1)

ss1 = {5,3,7,2,1,6}
ss2 = {1,4,6,2,7}

print(f"差集{ss1.difference(ss2)}")
print(f"并集{ss1.union(ss2)}")
print(f"交集{ss1.intersection(ss2)}")