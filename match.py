"""
day = input()
match day:
    case "1":
        print(f"今天是星期{str(day)},工作日")
    case "2":
        print(f"今天是星期{str(day)}工作日")
    case "3":
        print(f"今天是星期{str(day)},工作日")
    case "4":
        print(f"今天是星期{str(day)}工作日")
    case "5":
        print(f"今天是星期{str(day)},工作日")
    case "6":
        print(f"今天是星期{str(day)}休息日")
    case "7":
        print(f"今天是星期{str(day)},休息日")
    case _:
        print("输入错误")
"""

day = input("请输入数字1-7:")
match day:
    case "1"|"2"|"3"|"4"|"5":
        print(f"今天是星期{day},工作日")
    case "6"|"7":
        print({f"今天是星期{day},休息日"})
    case _:
        print("输入错误")