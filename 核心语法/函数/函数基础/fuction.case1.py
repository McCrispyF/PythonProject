"""
定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）。
定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分 (保留 1 位小数)，并返回。
"""

def area(low,high):
    total_area = low * high / 2
    return round(total_area, 2)

def alpha_num(str1):
    num = 0

    # for char in str1:
    #     if char.lower() in "aeiou":
    #         num += 1
    # return num

    return sum(1 for char in str1 if char.lower() in 'aeiou')


def score_calculate(scores):
    high = max(scores)
    low = min(scores)
    average = sum(scores) / len(scores)
    return round(high,1),round(low,1),round(average,1)

