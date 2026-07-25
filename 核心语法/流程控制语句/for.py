"""
a = "Hello World"
for c in a:
    print(c)
else:
    print(f"循环结束:{c}")
"""

"""
total = 0
for i in range(1,101):
    if i % 2 != 0:
        total += i
print (f"1到100的奇数累加之和为：{total}")
"""

total = 0
#range(start,end,step)
for i in range(1,101,2):
    total += i
print (f"1到100的奇数累加之和为：{total}")