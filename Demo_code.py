"""
1.九九乘法表
2.冒泡排序
3.1~100的和
4.分配列表变量
5.检查内存占用
6.交换变量
7.组合字符串
8.转换嵌套列表
9.转置矩阵
10.比较列表
"""



# @1.九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}x{i}={i*j}\t',end='')
#     print()



# # @2.冒泡排序
# def bubble_sort(list):
#     for i in range(0,len(list) - 1):
#         for j in range(i + 1,len(list)):
#             if list[i] > list[j]:
#                 list[i],list[j] = list[j], list[i]
#     return list
# print(bubble_sort(list=[7,85,1,5,3,55]))

# # 3.100内的和
# sum(i for i in range(1,101) )  #后加print
# # 或者 sum(range(1,101))

# 4.分配列表变量
# List = ["I","Love","Python"]
# a, b, c = List
# print(a,b,c )
# #I Love Python
# print(c,b,a )
# #Python Love I

# 5.检查内存占用
import sys
# a, b, c,d = "I" ,"Love", "Python", 2020
# print(sys.getsizeof(a))
# #50
# print(sys.getsizeof(b))
# #53
# print(sys.getsizeof(c))
# #55
# print(sys.getsizeof(d))
# #28

# 6.交换变量
# a,b = 'zaoqi' , 'Python'
# a,b = b,a


# 7.组合字符串
# List = ['I ', 'Love ', 'Python']
# print(''.join(List))
# #I Love Python


# 8.转换嵌套列表
# import itertools
# List = [[1, 2], [3, 4], [5, 6]]
# print(list(itertools.chain.from_iterable(List)))
# #[1, 2, 3, 4, 5, 6]

# 9.转置矩阵
# matrix = [[1, 2, 3], [4, 5, 6]]
# print(list(zip(*matrix)))
# #[(1, 4), (2, 5), (3, 6)]

# 10.比较列表
# a = ['I', 'Love', 'Python']
# b = ['I', 'Love', 'python']
# print(set(a).difference(set(b)))
# print(set(a).intersection(b))
# #{'Python'}
# #{'Love', 'I'}


