"""
根据提供的班级学生的选课情况，完成如下需求：
1．找出同时选修了法语和艺术的学生
2．找出同时选修了所有四门课程的学生
3．找出选修了足球，但是没有选修篮球的学生
4．统计每一个学生选修的课程数量
"""

#选修足球学生
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
#选修篮球学生
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
#选修法语学生
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
#选修艺术学生
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

print("方式一--------------------------------------")
print(f"同时选修法语和艺术：{french_set.intersection(art_set)}")
print(f"同时选修四门课的学生：{football_set.intersection(basketball_set.intersection(french_set.intersection(art_set)))}")
print(f"选修了足球没选修篮球的学生：{football_set.difference(basketball_set)}")
print("方式二--------------------------------------")
print(f"同时选修法语和艺术：{french_set&art_set}")
print(f"同时选修四门课的学生：{football_set&basketball_set&french_set&art_set}")
print(f"选修了足球没选修篮球的学生：{football_set - basketball_set}")
print("方式三--------------------------------------")#集合推导式:  {要往集合中添加的元素 for i in set1 if 条件}
football_set3 = {i for i in football_set if i not in basketball_set}
print(f"选修了足球没选修篮球的学生:{football_set3}")

print("-------------------------------------------")
#统计每一个学生选修的课程数量
#方法一   all_set = football_set.union(basketball_set.union(french_set.union(art_set)))
#方法二
all_set = football_set | basketball_set | french_set | art_set
print(all_set)
all_list = [*football_set,*basketball_set,*french_set,*art_set]#解包
print(all_list)

for i in all_list:
    print(f"{i}选修了{all_list.count(i)}门课程")