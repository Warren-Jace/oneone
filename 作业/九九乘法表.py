# for i in range(1, 10):
#     for j in range(i, 10):
#         sum = i * j
#         print("{} * {} = {}".format(i, j, sum))
#     print("\n")

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{} * {} = {:<3}   ".format(j, i, i*j), end="")
#     print("\n")

# 水仙花数
# num = eval(input("请输入一个三位数："))
# for num in range(100,1000):
#     if 99 < num < 1000:
#         c = num % 10
#         b = (num // 10) % 10
#         a = num // 100
#         sum = pow(a, 3)+pow(b, 3)+pow(c, 3)
#         if sum == num:
#             print("{}是水仙花数".format(num))
#         # else:
#         #     print("{}不是水仙花数".format(num))
#     else:
#         print("输入有误！")


# while(True):
#     try:
#         num = eval(input("请输入一个三位数："))
#     except NameError:
#         print("输入有误！")
#         break
#     # if isinstance(num, int):
#     c = num % 10
#     b = (num // 10) % 10
#     a = num // 100
#     sum = pow(a, 3) + pow(b, 3) + pow(c, 3)
#     if sum == num:
#         print("{}是水仙花数".format(num))
#     else:
#         print("{}不是水仙花数".format(num))


# max_num = int(input('请输入最大范围'))
# # 获取小于指定数的阿姆斯特朗数
# for num in range(0, max_num):
#     sum = 0
#     length = len(str(num))
#     temp = num
#     for i in range(length):
#         sum += (temp % 10) ** length
#         temp //= 10
#     if sum == num:
#         print(num)

#猜数字
from random import *
num = randint(1, 6)
count = 0
while(True):
    try:
        inde = eval(input("请输入一个0 - 10的数："))
    except NameError:
        print("非数字！")
        break
    if num == inde:
        print("猜对了!\n一共猜了{}次：".format(count))
        break
    else:
        count += 1
        print("猜错了！")