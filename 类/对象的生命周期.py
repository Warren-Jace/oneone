# class Person:
#     # def __new__(cls, *args, **kwargs):
#     #     print("lanjie")
#     def __init__(self):
#         print("初始化")
#         self.name = "sz"
#     def __del__(self):
#         print("shifang")
# p = Person()
# print(p)
# print(p.name)

class Person:
    pp = 0
    def __init__(self):
        # global pp
        self.pp += 1
        print("+1")
    def __del__(self):
        # global pp
        self.pp -= 1
        print("-1")
    # def log(self):
    #     print(pp)

    def log(self):
        print(self.pp)
p = Person()
# print(pp)
p.log()
del p
# print(pp)
Person.log()
