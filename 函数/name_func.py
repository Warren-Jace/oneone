# 匿名函数， 也称为lambda函数
# 语法lambda 参数1，参数2：表达式
res = (lambda x, y: x + y)(1, 2)
print(res)


nameFunc = lambda x, y: x + y
print(nameFunc(4, 5))

L = [{"name": "s1", "age": 11}, {"name": "ss", "age": 12}, {"name": "s3", "age": 17}, {"name": "ss", "age": 19}]

# def getKey(x):
#     return x["name"]

# result = sorted(L,key=getKey)
__result = sorted(L, key=lambda x: x["name"])
print(__result)
