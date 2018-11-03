# class Person:
#     def __call__(self, *args, **kwargs):
#         print("xx", args, kwargs)
#
# p = Person()
#
# p(12, 45, n = 12)

#
# def creatPen(p_type, p_color):
#     print("创建了一个%s画笔, 它是%s颜色" % (p_type, p_color))
#
# creatPen("ss", "ff")
# import functools
# pen = functools.partial(creatPen, p_type="gangbi")
#
# pen(p_color="red")

# class PenFactory:
#     def __init__(self, p_type):
#         self.p_type = p_type
#     def __call__(self, p_color):
#         print("bi:%s, yanse:%s" %(self.p_type, p_color))
#
# gb = PenFactory("gbb")
# gb("red")

# class Person:
#     def __init__(self):
#         self.cache = {}
#     def __setitem__(self, key, value):
#         # print("setitem", key, value)
#         self.cache[key] = value
#     def __getitem__(self, item):
#         # print("getitem", item)
#         return self.cache[item]
#     def __delitem__(self, key):
#         # print("delitem", key)
#         del self.cache[key]
# p = Person()
# p["name"] = "s2"
# print(p["name"])
# del p["name"]
# # print(p["name"])
# print(p.cache)

#
# class Person:
#     def __init__(self):
#         self.items = [1,2,3,4,5,6,7,8,9]
#     def __setitem__(self, key, value):
#         # print(key, value)
#         # print(key.start)
#         # print(key.stop)
#         # print(key.step)
#         # print(value)
#         if isinstance(key, slice):
#             self.items[key] = value
#     def __getitem__(self, item):
#         print("getitem", item)
#     def __delitem__(self, key):
#         print("delitem", key)
# p = Person()
# p[0: 4: 2] = ["a", "b"]
# # p[1: 5: 2]
# print(p.items)
#
# class Person:
#     def __init__(self, age, height):
#         self.age = age
#         self.height = height
#     def __eq__(self, other):
#         print(other)
#         return self.age == other.age
# p1 = Person(18,170)
# p2 = Person(20, 190)
# print(p1 == p2)

# class Person:
#     def __init__(self):
#         self.result = 1
#     def __getitem__(self, item):
#         self.result += 1
#         if self.result >= 6:
#             raise StopIteration("停止遍历")
#         return self.result
# p = Person()
# for i in p:
#     print(i)


# class Person:
#     def __init__(self):
#         self.result = 1
#     def __getitem__(self, item):
#         print("getitem")
#         self.result += 1
#         if self.result >= 6:
#             raise StopIteration("停止遍历")
#         return self.result
#     def __iter__(self):
#         print("iter")
#         # return iter([1, 2, 3, 4, 5])
#         return self
#     def __next__(self):
#         # print("getitem")
#         self.result += 1
#         if self.result >= 6:
#             raise StopIteration("停止遍历")
#         return self.result
# p = Person()
# for i in p:
#     print(i)

# class Age:
#     def __get__(self, instance, owner):
#         print("get")
#     def __set__(self, instance, value):
#         print("set")
#     def __delete__(self, instance):
#         print("delete")
#
# class Person:
#     age = Age()
    # def __init__(self):
    #     self.__age = 10
    # def get_age(self):
    #     return  self.__age
    # def set_age(self, value):
    #     if value < 0:
    #         value = 0
    #     self.__age = value
    # def del__age(self):
    #     del self.__age
    # age = property(get_age(), set_age(), del__age())
# # p = Person()
# # p.age = 10
# # print(p.age)
# # p.age = -1
# # p.del__age()
# # print(p.get_age())
# # p.age = 10
# # print(p.age)
# print(Person.age)
# Person.age = 10
# del Person.age

# def check(func):
#     def inner():
#         print("yz")
#         func()
#     return inner


# class check:
#     def __init__(self, func):
#         self.f = func
#     def __call__(self, *args, **kwargs):
#         print("aa")
#         self.f()
# @check
# def Preson():
#     print("ss")
# Preson = check(Preson)
#
# Preson()1

import objgraph
import gc
import weakref

class Person:
    pass
class Dog:
    pass


p = Person()
d = Dog()
p.pet = d
d.master = p
del p
del d
gc.disable()
gc.collect()
print(objgraph.count("Person"))
print(objgraph.count("Dog"))

