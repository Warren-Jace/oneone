# 返回函数

def getFunc(flage):
    # 定义几个函数
    # def sum(a, b, c):
    #     return a + b + c
    # def jian(a, b, c):
    #     return a - b - c
    # 根据flage的值，来返回不同的操作函数
    if flage == "+":
        return sum
    elif flage == "-":
        return jian

def sum(a, b, c):
    return a + b + c
def jian(a, b, c):
    return a - b - c
__result = getFunc("-")
# print(result, type(result))
res = __result(1, 2, 3)
print(res)