# _*_coding:utf-8_*_
# Author : oracle12c
# Time   : 2019/1/7 15:34
# File   : test.py
# IDE    : PyCharm

person = ['tony', ['savings', 100]]

p1 = person[:]
p2 = person[:]

print(p1, '***', p2)

p1[0] = 'tom'
p2[0] = 'lode'

p1[1][1] = 50

print(p1, '***', p2)


for i in (0,1,2,3,4,5,6,7,8):
    print(i)



