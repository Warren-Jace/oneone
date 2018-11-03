def zsq(func):
    def inner(*args, **kwargs):#元组和字典
        print("-"*20)
        #print(args, kwargs)
        res = func(*args, **kwargs)#拆包
        return res
    return inner
@zsq
def pnum(num, n2, num3):
    print(num, n2, num3)
    return num + n2 + num3

res1 = pnum(123, 456, num3=666)
print(res1)
