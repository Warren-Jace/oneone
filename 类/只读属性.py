# class Person:
#     def __init__(self):
#         self.__age = 18
#     # 可以使用属性的方式，使用这个方法
#     @property
#     def getAge(self):
#         return self.__age
#
#
# p1 = Person()
# # print(p1.getAge())
# print(p1.getAge)
# p1.age = 10
# print(p1.__dict__)
# # property
class Person:
    def __setattr__(self, key, value):
        print(key, value)
        if key == "age" and key in self.__dict__.keys():
            print("这个属性是只读属性")
        else:
            # self.key = value
            self.__dict__[key] = value


p1 = Person()
p1.age = 18
p1.age = 888
print(p1.age)
print(p1.__dict__)


















