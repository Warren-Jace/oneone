# 定义两个功能函数
# def fss():
#     print("发说说")
# def ftp():
#     print("发图片")
#
#
# # 逻辑代码
# n = 2
# if n == 1:
#     print("登录验证。。。")
#     fss()
# else:
#     print("登录验证。。。")
#     ftp()
# 登录验证
# 1.代码重用差


def checklogin(func):
    def inner():
        print("登录验证。。。")
        func()
    return inner
    # print("登录验证。。。")
    # return func()


@checklogin
def fss():
    print("发说说")

# fss = checklogin(fss)
@checklogin
def ftp():
    print("发图片")
# ftp = checklogin(ftp)

# 逻辑代码
n = 1
if n == 1:
    # print("登录验证。。。")
    fss()
else:
    # print("登录验证。。。")
    ftp()
