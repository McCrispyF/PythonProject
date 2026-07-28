"""
定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
具体规则如下：
优惠券需要商品金额满 5000 才可以使用，且优惠券金额不能超过商品总价。
积分抵扣需要商品总金额满 5000 才可以使用，100 积分抵扣 1 元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""

def cal(*args,coupon = 0,score = 0,express:float = 0) -> float:  #类型注解:int 和 -> float只是提示，不能改变python动态类型的事实
    """
    计算总金额的函数
    :param args:商品信息：商品名、价格、数量  如("鼠标"，299，2）
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 总金额
    """
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    if 5000 <= coupon <= total_cost:
        total_price -= coupon

    if 5000 <= score // 100 <= total_cost:   #//代表整除
        total_price -= score // 100

    total_cost += express

    return total_cost

total = cal(("鼠标",188,2),("键盘",388,1),("耳机",3999,1),coupon = 10,score = 4000,express = 9.9)
print(total)