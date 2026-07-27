# 邮箱格式验证:用户输入一个邮箱，验证邮箱格式是否正确(包含一个@和至少一个.) 如果输入正确输出"邮箱格式正确"，否则输出"邮箱格式错误"

user_input = input("请输入邮箱：")

at_amount = user_input.count("@")
dot_amount = user_input.count(".")

# if at_amount == 1 and dot_amount >= 1:
#     print(f"{user_input}邮箱格式正确")
# else:
#     print(f"{user_input}邮箱格式错误")

if at_amount == 1 and "." in user_input:
    print(f"{user_input}邮箱格式正确")
else:
    print(f"{user_input}邮箱格式错误")