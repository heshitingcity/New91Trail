#-*- coding:utf-8 -*-
# @author  : City
# @datetime: 2020/10/22 16:45
# @File    : 001.py


# listb = []
# A = input("请输入5个随机数：")
# listb = list(set(A))
# print(listb)
#
# #冒泡排序
# def MP(lista):
#     n = len(lista)
#     for i in range(n):
#         for j in range(0,n-1):
#             if lista[j]>lista[j+1]:
#                 lista[j],lista[j+1] = lista[j+1],lista[j]
#     return lista
#
#
# lista = [12,55,3,66,7,43,88,34]
#
# MP(lista)
# print(lista)
#
#
#
#
#
# #斐波那契数列
#
# import sys
# def fibonacci(n): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# fa = fibonacci(int(input('请输入n的值：'))) # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print (next(fa), end=" ")
#     except StopIteration:
#         sys.exit()




# myList = [1,4,5,0,6]
# for i in range(0,len(myList)):
#     for j in range(0,len(myList)-1):
#         if myList[j]>myList[j+1]:
#             myList[j],myList[j+1] = myList[j+1],myList[j]
# print(myList)

import random

# 随机生成姓名
# def random_name():
#     xing = "赵钱孙李周吴郑王"
#     ming = '圣诞节李书磊色黑喜欢恩格尔恒瑞欧文荣二维画金芙蓉未'
#     x = random.choice(xing)
#     m = ''.join(random.choice(ming) for i in range(1, 3))
#     print(x + m)
#     return x + m
#
#
# # 随机生成手机号
# def random_phoneNumber():
#     start_numb = '131,176,156'
#     end_numb = '0123456789'
#     S_numb = random.choice(start_numb.split(','))
#     E_num = ''.join(random.choice(end_numb) for i in range(0, 8))
#     print(S_numb + E_n