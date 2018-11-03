# L = [{"name": "s1", "age": 11}, {"name": "ss", "age": 12}, {"name": "s3", "age": 17}, {"name": "ss", "age": 19}]
#
# def getKey(x):
#     return x["name"]
#
# result = sorted(L,key=getKey)
# print(result)
#
def caculate(num1, num2, caculatefunc):
    print(caculatefunc(num1,num2))

# def sum(a, b):
#     return a + b
# def jianfa(a, b):
#     return a - b
caculate(1, 2, lambda a, b: a + b)