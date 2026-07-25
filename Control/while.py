"""
print("while循环测试\n")
a = 0
while a < 10:
    print(a)
    a += 1
else:
    print(f"循环结束，当前是{a}")
"""

i = 0
total = 0
while i <= 100:
    if i % 2 == 0:
        total = total + i
    i += 1
print(total)