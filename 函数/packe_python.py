# 闭包：在函数嵌套的前提下内层函数引用外层函数的变量（包括参数）
# 外层有把内层函数作为返回值进行返回

# def test():
#     a = 10
#     def test2():
#         print(a)
#     return test2
# ss = test()
# ss()

# def line_config(content, length):
#     def line():
#         print("*"*(length // 2) + content + "*"*(length // 2))
#         return line
#
# line_config("sd", 20)

# def test():
#     a = 10
#     def test2():
#         # 闭包中如果要使用和修改外部变量，需要用nonlocal声明，否则则会认为是闭包中新定义的变量
#         nonlocal a
#         a = 666
#         print(a)
#     print(a)
#     test2()
#     print(a)
#     return test2
# ss = test()
# ss()


# def test():
#     a = 1
#     def test2():
#         print(a)
#     a = 2
#     return test2
# newFunc = test()
# newFunc()
# 函数什么时候才会被确定内部变量标识对应的值
# 当函数被调用的时候，才会正真的确定对应的值到底是什么，之前都是以不同的变量标识名称存在
# def test():
#     funcs = []
#     for i in range(1, 4):
#         def test2():
#             a = i
#             print(a)
#         funcs.append(test2)
#     return funcs
#
#
# newFuncs = test()
# print(newFuncs)
#
# newFuncs[1]()
# newFuncs[2]()
# newFuncs[0]()

def test():
    funcs = []
    for i in range(1, 4):
        def test2(num):
            def inner():
                print(num)
            return inner
        funcs.append(test2(i))
    return funcs


newFuncs = test()
print(newFuncs)

newFuncs[1]()
newFuncs[2]()
newFuncs[0]()