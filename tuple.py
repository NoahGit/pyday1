# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2019/1/7 16:59
# File   : tuple.py
# IDE    : PyCharm


# # 元组-被称为只读列表，只能查、切片，不能修改。
# names = ('tony', 'jone', 'god')
# # 元组两个方法，count和index
#
# print(names)
# print(names.count('god'))
# print(names.index('god'))




# 购物车
# 程序：购物车程序
#
# 需求:
#
# 1.启动程序后，让用户输入银行卡余额，然后打印商品列表.
# 2.允许用户根据商品编号购买商品.
# 3.用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒.
# 4.可随时退出，退出时，打印已购买商品和余额.

goods = [[10123, 'iphone', 8000], [12698, 'python book', 90], [15874, 'pc', 1000], [16984, 'shoes', 599]]
goodsNo = []
shopping_Cart = []
for i in goods:
    goodsNo.append(i[0])
print(goodsNo)
pay = input("\033[33;1m请输入银行卡余额：\033[0m")
if pay.isdigit():
    pay = int(pay)
    while True:
        print("\033[32;1m购物车有：%s 等商品。\033[0m" %(shopping_Cart))
        for index, item in enumerate(goods):
            print(index, item)
        num = input("\033[33;1m请输入想购买的商品编号：，退出请按q回车\033[0m")
        if num.isdigit() and int(num) in goodsNo:
            goods_index = goodsNo.index(int(num))
            if pay >= goods[goods_index][2]:
                pay = pay - goods[goods_index][2]
                shopping_Cart.append([goods[goods_index][0], goods[goods_index][1], goods[goods_index][2]])
                print("\033[31;1m已经购买 %s 成功，花费了 %s 元，卡里还剩 %s 元。\033[0m" %(goods[goods_index][1], str(goods[goods_index][2]), str(pay)))
            elif pay > 90 and pay < goods[goods_index][2]:
                print("\033[32;1m余额不足，请重新输入另外一种商品编号\033[0m")
            else:
                print("\033[32;1m任何商品都买不了了\033[0m")
                print("----------shopping list----------")
                for i in shopping_Cart:
                    print("\033[32;1m %s \033[0m" % i)
                break
        elif num == 'q':
            print("----------shopping list----------")
            for i in shopping_Cart:
                print("\033[32;1m %s \033[0m" %i)
            break
        else:
            print("\033[32;1m编号不存在，请重新输入\033[0m")
else:
    print("\033[33;1m请重新输入银行卡余额：\033[0m")