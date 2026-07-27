"""
根据提供的学生成绩单，完成如下需求：
1．计算每个学生的总分、各科平均分，然后一并输出出来。
2．统计各科成绩的最低分、最高分、平均分，并输出。
3．查找成绩优秀（平均分大于 90）的学生，并输出。
"""
from asyncio import start_unix_server

"""
学号	    姓名	   语文     数学	   英语
S001	王林	    85	    92	    78
S002	李慕婉	92	    88	    95
S003	十三	    78	    85	    82
S004	曾牛	    88	    79	    91
S005	周轶	    95	    96	    89
S006	王卓	    76	    82	    77
S007	红蝶	    89	    91	    94
S008	徐立国	75	    69	    82
S009	许木	    86	    89	    98
S010	遁天	    66	    59	    72
"""

"""
class Student:
    def __init__(self, stu_num, name, chinese, math, english):
        self.stu_num = stu_num
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def score_calculate(self):
        print(self.stu_num)
        total = self.math + self.english
        average = total / 3
        print(f"学生 {self.name} 的 平均成绩是 {average} 总计是 {total}")

p = Student("S001","王林",85,92,78)
p.score_calculate()
"""

students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

#1．计算每个学生的总分、各科平均分，然后一并输出出来。
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
#方式一
# for i in students:   # i 也是元组
#     total = i[2] + i[3] + i[4]
#     average = total / 3
#     print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]} \t {i[4]} \t {total} \t{average:.2f}")    #  {average:.2f}  保留两位小数，f代表float浮点数

#方式二 元组解包
for id_,name,chinese,math,english in students:   # i 也是元组
    total = chinese + math + english
    average = total / 3
    print(f"{id_} \t {name} \t {chinese} \t {math} \t {english} \t {total} \t{average:.2f}")



print("\n\n")

#2．统计各科成绩的最低分、最高分、平均分，并输出。
list_chinese = [i[2] for i in students]
list_math = [i[3] for i in students]
list_english = [i[4] for i in students]

print(f"语文的最低分：{min(list_chinese)}  最高分：{max(list_chinese)}  平均分：{sum(list_chinese)/len(list_chinese):.2f}")
print(f"数学的最低分：{min(list_math)}  最高分：{max(list_math)}  平均分：{sum(list_math)/len(list_math):.2f}")
print(f"英语的最低分：{min(list_english)}  最高分：{max(list_english)}  平均分：{sum(list_english)/len(list_english):.2f}")

#3．查找成绩优秀（平均分大于 90）的学生，并输出。

# for i in students:
#     scores = [i[2], i[3], i[4]]
#     avg = sum(scores) / len(scores)
#     if avg > 90:
#         print(f"{i[1]}同学是优秀学生")

for id_,name,chinese,math,english in students:
    scores = [chinese, math, english]
    avg = sum(scores) / len(scores)
    if avg > 90:
        print(f"{name}同学是优秀学生")