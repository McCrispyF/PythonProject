import random
num = random.randint(1,100)

while True:
    try:
        a = int(input("请猜1-100数字："))
    except ValueError:
        print("输入错误，请输入数字：")
        continue
    if a == num:
        print(f"猜对啦，答案是{num}")
        break
    elif a > num:
        print("猜大了")
    elif a < num:
        print("猜小了")