# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2019/1/7 16:59
# File   : tuple.py
# IDE    : PyCharm

print('开始')

'''
# 元组-被称为只读列表，只能查、切片，不能修改。
names = ('tony', 'jone', 'god')
# 元组两个方法，count和index

print(names)
print(names.count('god'))
print(names.index('god'))
'''


'''
购物车
程序：购物车程序

需求:

1.启动程序后，让用户输入银行卡余额，然后打印商品列表.
2.允许用户根据商品编号购买商品.
3.用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒.
4.可随时退出，退出时，打印已购买商品和余额.
'''
goods = [[10123, 'iphone', 8000], [12698, 'python book', 90], [15874, 'pc', 1000], [16984, 'shoes', 599]]
goodsNo = [10123, 12698, 15874, 16984]
while True:
    pay = input("请输入银行卡余额：")
    for i in goods:
        print(i)
    num = input("请输入想购买的商品编号：")
    if int(num) in goodsNo:
        goods_index = goodsNo.index(int(num))
        if int(pay) >= goods[goods_index][2]:
            pay_now = int(pay) - goods[goods_index][2]
            print("已经购买" + goods[goods_index][1] + "成功，花费了" + str(goods[goods_index][2]) + "元，卡里还剩" + str(pay_now) + "元。")
        else:
            print("余额不足，请重新输入编号")
    else:
        print("编号不存在，请重新输入")




    # for number in (goods[0][0], goods[1][0], goods[2][0], goods[3][0]):
    #     if int(num) == number:
    #         if int(pay) >= goods[0][2]:
    #             pay_now = int(pay)-goods[0][2]
    #             print("已经购买"+goods[0][1]+"成功，花费了"+str(goods[0][2])+"元，卡里还剩"+str(pay_now)+"元。")
    #         else:
    #             print("您的余额不足，无法购买此商品。")