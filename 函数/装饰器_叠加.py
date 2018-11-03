#从上到下去装饰
# 从下到上去执行，有点类似递归
# def z_line(func):
#     def inner():
#         print("----------")
#         func()
#     return inner
#
# def z_start(func):
#     def inner():
#         print("**********")
#         func()
#     return inner
# @z_line#再执行
# @z_start#先执行
# def print_content():
#     print("房管局欧舒丹")
#
# print_content()



# def zsq(func):
#     def inner():
#         print("-"*20)
#         func()
#     return inner
# @zsq#不能装饰有参数的函数
# def pnum():
#     print(10)
# # pnum = zsq(pnum)
# pnum()

# 有参数的装饰
# def zsq(func):
#     def inner(n, n2):
#         print("-"*20)
#         func(n,n2)
#     return inner
# @zsq
# def pnum(num, n2):
#     print(num,n2)
# # pnum = zsq(pnum)
# pnum(123,456)

def zsq(func):
    def inner(*args, **kwargs):#元组和字典
        print("-"*20)
        print(args, kwargs)
        func(*args, **kwargs)#拆包
    return inner
@zsq
def pnum(num, n2, num3):
    print(num, n2, num3)
# pnum = zsq(pnum)

pnum(123, 456, num3=666)


