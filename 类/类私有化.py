# class Animal:
#     _x = 10
#
#     def test(self):
#         print(Animal._x)
#         print(self._x)
#     pass
#
#
# class Dog(Animal):
#     def test2(self):
#         print(Dog._x)
#         print(self._x)
#     pass
#
#
# a = Animal()
# # a.test()
# #
# # d = Dog()
# # d.test2()
#
# print(Animal._x)
# print(Dog._x)
# print(a._x)
# # print(d._x)
#
# # a = 666

class Person:
    """初始化"""
    def __init__(self):
        self.__age = 18
    def setAge(self,value):
        if isinstance(value, int) and 0 < value < 200:
            self.__age = value
        else:
            print("输入有误，请重新输入")
    def getAge(self):
        return self.__age
p1 = Person()
p1.setAge(200)
print(p1.getAge())
p2 = Person()
p3 = Person()

# print(p1.age)
# print(p2.age)
# print(p3.age)
# print(p1.__dict__)


















