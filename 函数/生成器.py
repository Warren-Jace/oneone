# l = [i for i in range(1, 100000) if i % 2 == 0]
# 生成器
# l = (i for i in range(1, 100000) if i % 2 == 0)
#
# print(next(l))
# print(next(l))
# print(l.__next__())
# for i in l:
#      print(i)


# yied, 可以去阻断当前的函数执行, 然后, 当使用next()函数, 或者, __next__(), 都会让函数继续执行, 然后, 当执行到下一个 yield语句的时候, 又会被暂停
# def test():
#     print("123")
#     yield 1
#     print("a")
#     yield 2
#     print("b")
#     yield 3
#     print("c")
#     yield 4
#     print("d")
#     yield 5
#     print("e")
#     yield 6
# test1 = test()
# print(next(test1))
# print(next(test1))
# print(next(test1))
# print(next(test1))
# print(next(test1))
# print(next(test1))

def test():
    res1 = yield 1# = "000"
    print(res1)

    res2 = yield 2
    print(res2)

g = test()
# print(g.__next__())
# print(g.__next__())
# print(g.send("000"))
print(g.send(None))
