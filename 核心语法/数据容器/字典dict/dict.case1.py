"""
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
5.退出购物车
"""

#结构：shopping_cart = {"Mate80":{"price":30,"num":50}}

shopping_cart = {}

menu = """
##########购物车系统###########
#        1.添加购物车         #
#        2.修改购物车         #
#        3.删除购物车         #
#        4.查询购物车         #
#        5.展示购物车         #
#        6.退出购物车         #
##########购物车系统###########
"""
print("欢迎使用购物车管理系统")
print(menu)

while True:
    user_input = input("请选择执行的操作（1-5）：")
    match user_input:
        case "1":  # 添加购物车
            try:
                good_name = input("请输入商品名称：")
                good_price = float(input("请输入商品价格："))
                good_num = int(input("请输入商品数量："))
                if good_name in shopping_cart:
                    print(f"商品{good_name}已存在，请重新选择")
                else:
                    shopping_cart[good_name] = {"price": good_price, "num": good_num}
                    print(f"商品{good_name}添加成功")
            except ValueError:
                print("输入错误！")
        case "2":  # 修改购物车
            good_name = input("请输入需要修改的商品名称：")
            if good_name not in shopping_cart:
                print(f"商品{good_name}商品不存在")
            else:
                try:
                    good_price = float(input("请输入要修改的商品价格："))
                    good_num = int(input("请输入要修改的商品数量："))
                    shopping_cart[good_name] = {"price": good_price, "num": good_num}
                    print(f"商品{good_name}修改成功")
                except ValueError:
                    print("输入错误")
        case "3":  # 删除购物车
            good_name = input("请输入需要删除的商品名称：")
            if good_name not in shopping_cart:
                print(f"商品{good_name}商品不存在")
            else:
                del shopping_cart[good_name]
                print(f"商品{good_name}删除成功")
        case "4":  # 查询购物车
            good_name = input("请输入需要查询的商品名称：")
            if good_name in shopping_cart:
                goods_info = shopping_cart[good_name]
                print(f"成功查询到{good_name}，价格：{goods_info["price"]}，数量：{goods_info["num"]}")   #Python 3.11 及更早：引号需要用外双内单
            else:
                print(f"未查询到{good_name}")
        case "5":
            if len(shopping_cart) == 0:
                print("购物车是空的")
            else:
                for good_name, goods_info in shopping_cart.items():
                    print(f"商品名称：{good_name}商品价格：{goods_info['price']}商品数量：{goods_info['num']}")
        case "6":  # 退出购物车
            print("Bye")
            break
        case _:
            print("非法操作")
