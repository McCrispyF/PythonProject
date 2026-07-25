#将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值。
nums = []
i = 0
while i < 10:
    try:
        a = int(input(f"请输入十个数字(第{i + 1}个):"))
        nums.append(a)
        i += 1
    except ValueError:print("输入错误，请输入数字")
print(nums)
TempList = sorted(nums)
print(f"最小值为：{nums[0]}")
print(f"最大值为：{nums[-1]}")
average = sum(nums) / len(nums)
print(f"平均值为：{average}")