"""
leetcode hot100 #1
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。


nums:list[int] = [2, 7, 11, 15]
target: int = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)
"""

a = int(input("请输入长度："))
b = int(input("请输入宽度："))
for i in range(a):
    for j in range(b):
        print("*",end = "  ")
    print("\n",end = "")