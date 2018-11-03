# class Person:
#     def __init__(self):
#         self.__age = 18
#
#     def get_age(self):
#         return self.__age
#     def set_age(self,value):
#         self.__age = value
#
#     age = property(get_age, set_age)
#
#
# p = Person()
# print(p.age)
# p.age = 90
# print(p.age)
# print(p.__dict__)

# 第二种方式
# class Person:
#     def __init__(self):
#         self.__age = 18
#     @property
#     def age2(self):
#         return self.__age
#     @age2.setter
#     def age1(self, Value):
#         self.__age = Value
# p = Person()
# print(p.age2)
# p.age1 = 10
# print(p.age2)

