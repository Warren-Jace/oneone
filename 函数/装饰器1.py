# 1、函数名字不能改变
# 2.函数体内的代码不能发生改变
def check(func):
    def inner():
        print("登录验证。。。")
        func()
    return inner
@check #立即执行
def fss():
    print("发说说")
fss()