#判断字符吃饭是否对称
str_demo = "上海自来水来自海上"
str_reserve = str_demo[::-1]
if str_demo == str_reserve:
    print(f'"{str_demo}" 是对称的')
else:
    print(f"\"{str_demo}\" 非对称")

#将用户输入的10个字符串，全部转化为大写并且反转，然后记录到列表中，最后遍历输出列表内容
str_list = []
for i in range(1,11):
    user_input = input(f"请输入10个字符串的第{i}个:")
    user_upper = user_input.upper()
    user_reverse = "".join(reversed(user_upper))
    str_list.append(user_reverse)

for j in range(len(str_list)):
    print(str_list[j])