# 带有参数的装饰器
def getzsq(char):
    def zsq(func):
        def inner():
            print(char*30)
            func()
        return inner
    return zsq

# def zsq1(func):
#     def inner():
#         print("="*30)
#         func()
#     return inner
#
# def zsq2(func):
#     def inner():
#         print("-"*30)
#         func()
#     return inner
@getzsq("*")
def f1():
    print("666")
f1()